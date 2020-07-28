# Django Http utilities
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

# User authentication functionality 
# Login Required from class-based views
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

# Support Generic Views
from django.views import generic

# Support time zones
from django.utils import timezone

# Import models
from emp.models import Employee, Task, Job

# Import forms
from .forms import EmployeeForm, UserForm


class TestView(LoginRequiredMixin, generic.edit.FormView):
    template_name = 'accounts/dash_test.html'
    form_class = EmployeeForm
    context_object_name = 'test'
    success_url = '/test/'

    def form_valid(self, form):
        pass

    def get_queryset(self):
        return {}

class ProfileView(LoginRequiredMixin, generic.ListView):
    model = Employee

    template_name = 'accounts/profile.html'
    context_object_name = 'profile'

    def get_queryset(self):

        created = Employee.objects.get(user=self.request.user) != None
        return { 
                'user' : self.request.user, 
                'fields' : Employee._meta.get_fields(),
                'created' : created,
                }

class EditView(LoginRequiredMixin, generic.edit.FormView):

    template_name = 'accounts/edit_profile.html'
    form_class = EmployeeForm
    context_object_name = 'profile'
    success_url =  '/accounts/profile/'

    def form_valid(self, form):
        if Employee.objects.get(user=self.request.user):
            e = Employee.objects.get(user=self.request.user)
            e.middle_name = form.cleaned_data['middle_name']
            e.save()

        else:
            e = Employee.objects.create(user_id = self.request.user.id, dob="1998-01-21")
            e.middle_name = form.cleaned_data['middle_name']
            e.save()
        return super().form_valid(form)

    def get_queryset(self):
        return {}

class DashboardView(LoginRequiredMixin, generic.ListView):
    template_name = 'accounts/dashboard.html'

    def get_queryset(self):
        tasks = Task.objects.filter()

        return {}

class JobsView(LoginRequiredMixin, generic.ListView):
    model = Job
    template_name = 'accounts/jobs.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)

class JobView(LoginRequiredMixin, generic.DetailView):
    model = Job
    template_name = 'accounts/job.html'

class TasksView(LoginRequiredMixin, generic.ListView):
    model = Task

    template_name = 'accounts/tasks.html'

    context_object_name = 'profile'

    def get_queryset(self):
        tasks = [ task for task in Task.objects.all() if 
                task.job.user.username == self.request.user.username ]
        return { 'tasks' : tasks}

class TimesheetView(LoginRequiredMixin, generic.ListView):
    template_name = 'accounts/timesheet.html'

    def get_queryset(self):
        return {}

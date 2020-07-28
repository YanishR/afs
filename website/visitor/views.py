# Django imports
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views import generic

# Model imports
from .models import Service, SiteConfiguration, ServiceDetail, Homepage

# Form imports
from .forms import ContactForm

# Email imports
from django.core.mail import send_mail

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'visitor/homepage.html'

    context_object_name = 'home'

    def get_queryset(self):
        return { 'text': Homepage.objects.get(id=1), 
                'services': Service.objects.filter(display=True)}

class TestView(generic.ListView):
    template_name = 'visitor/test.html'

    context_object_name = 'test'

    def get_queryset(self):
        return {}

class AboutView(generic.ListView):
    template_name = 'visitor/company.html'

    context_object_name = 'company'

    def get_queryset(self):
        return {}

class CareersView(generic.ListView):
    template_name = 'visitor/careers.html'

    context_object_name = 'careers'

    def get_queryset(self):
        return {}

class ServicesView(generic.ListView):
    template_name = 'visitor/services.html'
    context_object_name = 'services'
  
    
    def get_queryset(self):
        return Service.objects.all()

class DetailView(generic.DetailView):

    model = Service 

    template_name = 'visitor/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return { 'service' : context['service'],
                'details' :  ServiceDetail.objects.filter(service=context['service'].rank)
                }

class ContactView(generic.edit.FormView):
    template_name = 'visitor/contact.html'

    form_class = ContactForm 
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            print("sending email")
            form.send_email()

        return super().form_valid(form)

    def form_invalid(self, form):
        print("form invalid")
        print(form.errors)
        response = super().form_invalid(form)
        print(form.cleaned_data['subject'])
        return response

class ContactSuccessView(generic.ListView):
    template_name = 'visitor/contact-success.html'


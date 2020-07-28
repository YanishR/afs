# Import django admin utility
from django.contrib import admin

# Import User utilities 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Import employee models for management
from .models import Employee, Task, Client, Job

from .models import Choice, Question

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

class TaskInline(admin.TabularInline):
    model = Task
    can_delete = True
    verbose_name = 'task'
    extra = 2

    fields = ['task_title', 'instructions']

class JobAdmin(admin.ModelAdmin):
    model = Job
    fieldsets = [
            (None, {'fields' : ['job_title'], }),
            ('Client', {'fields' : ['client'], }),
            ('Date Information', {'fields' : ['time_due'], }),
            ('Employee ', {'fields' : ['user']}),
            ]
    
    inlines = [ TaskInline ]

    list_display =  ('id', 'job_title', 'client', 'time_created')

    list_filter = [ 'client' ]

class ClientAdmin(admin.ModelAdmin):
    model = Client
    can_delete = True
    verbose_name = 'client'

    fields = ['name',]

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields' : ['question_text']}),
            ('Date Information', {'fields' : ['pub_date'], 'classes': ['collapse']}),
            ]
    inlines = [ChoiceInLine]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter =  ['pub_date']

    search_fields = ['question_text']

# Register all models here.
# User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Client
admin.site.register(Client)

# Job and Task
admin.site.register(Job, JobAdmin)
admin.site.register(Task)

admin.site.register(Question, QuestionAdmin)

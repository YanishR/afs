# Import forms
from django import forms
# Import Employee
from emp.models import Employee
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields  = ['first_name', 'last_name', 'email']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['middle_name']
        #exclude = ['user', 'saved', 'job_title']

class GlobalForm():
    pass

# Import models to make django models
from django.db import models

# To create employees from users
from django.contrib.auth.models import User

# Date and time utilities
from django.utils import timezone
import datetime


class Client(models.Model):

    name = models.CharField(max_length=30)
    #brn_number = models.CharField(max_length=12)

    # type of shareholders: company, individual, trust, directors
    # brn number, registered address
    # date of incorporation
    # financial year end
    # vat registration number
    # 

    def __str__(self):
        return self.name

class Employee(models.Model):
    saved = models.BooleanField(default=True)

    # Link to a user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Name of Employee
    middle_name = models.CharField(blank=True, max_length=30)
    maiden_name = models.CharField(blank=True, default="", max_length=30)

    # list for sex response
    SEX = [
            ('F', 'Female'),
            ('M', 'Male'),
        ] 
    sex = models.CharField(max_length=1, choices=SEX)
    dob = models.DateField('Date of Birth', blank=True)
    number_of_children = models.PositiveSmallIntegerField(default=0)

    job_title = models.CharField(max_length=30)

    # list for binary responses
    BINARY_RESPONSE = [ 
            ('Y', 'Yes'),
            ('N', 'No'),
            ]

    dependent = models.CharField(max_length=1, choices=BINARY_RESPONSE)
    nic = models.CharField(max_length=12)

    # emergency_number = models.
    # Previous employer, dates of employment
    # Tertiary education
    # Interests
    # Special skills
    # Languages
    # Address
    # Driving License
    # Renting/ 
    # Next of Kin
    # Banking Details
    # Emergency phone number
    # Phone number
    # Personal email address

    def __str__(self):
        return self.user.last_name + ', ' + self.user.first_name

class Job(models.Model):
    job_title = models.CharField(max_length=30)

    # Employee or employees task is associated to
    user = models.ForeignKey(User, 
            default=None,
            on_delete=models.CASCADE,
            verbose_name="employee tasked")

    # Client task is associated to
    client = models.ForeignKey(Client, 
            default=None,
            on_delete=models.CASCADE,
            verbose_name="client task")

    # Time at which task has been created
    time_created = models.DateTimeField(auto_now_add=True)

    # Due time
    time_due = models.DateTimeField(default=timezone.now)

    # Is task completed
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.job_title

    def getJobNumber(self):
        return job_id

    def getTasks(self):
        return Task.objects.filter(job=self)

    def isComplete(self):
        pass

# Model for tasks assigned to employees
# A Task also has a client assigned to
class Task(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    # Task title
    task_title = models.CharField(max_length=100)

    # Task instructions
    instructions = models.CharField(max_length=1000)

    # Time at which task has been created
    time_created = models.DateTimeField(auto_now_add=True)

    # Due time
    time_due = models.DateTimeField(default=timezone.now)

    # Is task completed
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title

    def time_published(self):
        return time 

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published Recently?"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

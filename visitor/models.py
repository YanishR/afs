from django.db import models

# Create your models here.

class Service(models.Model):
    rank = models.AutoField(primary_key=True)

    name = models.CharField(max_length=30)

    short_description = models.CharField(max_length=500)

    long_description = models.CharField(default=" ", max_length=2000)

    display = models.BooleanField(default=False)

    icon = models.CharField(default=" ", max_length=20)
    

    def __str__(self):
        return self.name

class ServiceDetail(models.Model):

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    name = models.CharField(max_length=20)

    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SiteConfiguration(models.Model):
    company_name = models.CharField(default=" ", max_length=30)
    abbreviation = models.CharField(default=" ", max_length=8)

    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name

    def clean(self):
        model = self.__class__
        if model.objects.count() > 0 and self.id != model.objects.get().id:
            raise ValidationError(
                    "Can only create one instance of " + model.__name__)

class Homepage(models.Model):
    our_firm = models.CharField(verbose_name="Our Firm", max_length=2000)
    about_us = models.CharField(verbose_name="About Us", max_length=2000)
    resume = models.CharField(verbose_name="Resume Of the Director", max_length=2000)

    def __str__(self):
        return "Homepage"

    def clean(self):
        model = self.__class__
        if model.objects.count() > 0 and self.id != model.objects.get().id:
            raise ValidationError(
                    "Can only create one instance of " + model.__name__)
    
class AboutUs(models.Model):
    pass

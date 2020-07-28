from django import forms

# Email imports
from django.core.mail import send_mail

class ContactForm(forms.Form):
    class Meta:
       pass
   
    name = forms.CharField(label='Name', max_length=40)
    email = forms.EmailField(label='Email')

    subject = forms.CharField(label='Subject', max_length=30)

    enquiry = forms.CharField(label='Enquiry Description', max_length=500)

    def send_email(self):
        print(self.cleaned_data['name'])
        print(self.cleaned_data['email'])
        print(self.cleaned_data['subject'])
        print(self.cleaned_data['enquiry'])
        send_mail(
            "Enquiry from " + self.cleaned_data['name'],
            self.cleaned_data['subject'] +\
            "\n ----------------------------------------------- \n" +\
            self.cleaned_data['enquiry'] +\
            "\n ----------------------------------------------- \n" +\
            "Email address: "  + self.cleaned_data['email'],
            "yanishrambocus@gmail.com",
            ["info@afsgroup.mu"],
            fail_silently=False)

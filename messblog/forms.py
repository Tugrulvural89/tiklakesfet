from django import forms
from django.forms import ModelForm

class MailForm(forms.Form):
    form_email = forms.EmailField(required=True,
                                    label="",
        widget=forms.EmailInput(attrs={'placeholder':'email', 'size':30 ,'rows':1, 'cols':10},))

class findallForm(forms.Form):
    url = forms.CharField(max_length=100)

from django import forms
from portfolio.models import Contact
from django.forms.widgets import TextInput, Textarea
from django.utils.translation import ugettext_lazy as _


class ContactMailSend(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'air_name': TextInput(attrs={'class': 'required form-control', 'placeholder': "What's your full name?"}),
            'air_email': TextInput(
                attrs={'class': 'required form-control', 'placeholder': "What's your permanent E-mail address?"}),
            'air_phone': TextInput(
                attrs={'class': 'required form-control', 'placeholder': "What's your active Mobile number?"}),
            'air_subject': TextInput(
                attrs={'class': 'required form-control', 'placeholder': "What's your reason for contacting me?"}),
            'air_message': Textarea(
                attrs={'class': 'required form-control', 'placeholder': "Write your queries here!"}),
        }
        error_messages = {
            'air_name': {
                'required': _("Name field is required."),
            },
            'air_email': {
                'required': _("Email field is required."),
            },
            'air_phone': {
                'required': _("Phone field is required."),
            },
            'air_subject': {
                'required': _("Subject field is required."),
            },
            'air_message': {
                'required': _("Message field is required."),
            },
        }
        labels = {
            "EMAILID": "E-mail",
            "MESSAGE": "what's in your mind?"
        }

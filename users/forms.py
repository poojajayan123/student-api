from django import forms
from django.forms.widgets import Textarea, TextInput, EmailInput
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# class ContactForm(forms.ModelForm):
    
#     class Meta:
#         model = User
#         fields = ['name','email','phone','comments']
#         widgets = {
#             'name': TextInput(attrs={'class': 'required','placeholder' : 'Name'}),
#             'phone': TextInput(attrs={'class': 'required','placeholder' : 'Phone'}),
#             'email': TextInput(attrs={'class': 'required email','placeholder' : 'Email'}),
#             'comments': Textarea(attrs={'class': 'required','placeholder' : 'Comments'}),
#         }
#         error_messages = {
#             'name' : {
#                 'required' : _("Name field is required."),
#             },
#             'comments' : {
#                 'required' : _("Comments field is required."),
#             },
#             'email' : {
#                 'required' : _("Email field is required."),
#             },
#             'phone' : {
#                 'required' : _("Phone field is required."),
#             }
#         }
from django import forms
from django.forms import widgets

from webapp.models import STATUS_CHOICES


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Description')
    full_description = forms.CharField(max_length=1000, required=False, label='Full_description',
                                       widget=widgets.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Status')
    finish_at = forms.DateField(required=False, label='Finish_at')

# Import django forms and models

from django import forms
from django.utils.html import strip_tags

from .models import Chirp

class ChirpForm(forms.ModelForm):
  body = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Chirp', 'class': 'form-control'}))
 
  class Meta:
    model = Chirp
    exclude = ('user',)
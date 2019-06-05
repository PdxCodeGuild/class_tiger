from django import forms
from chirp.models import Chirp

class NewChirpForm(forms.ModelForm):
    auto_id = False 
    text = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'new-text', "placeholder":"What's Happening?" }))

    class Meta:
        model = Chirp
        fields = ["text",]
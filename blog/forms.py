from django import forms
from .models import *


class BlogForm(forms.ModelForm): 
    class Meta:  
        model = BlogModel 
        fields = [ "title", "description"] 
        widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'cols':20}),
        }


class Subscribe(forms.Form):
    Email = forms.EmailField()
    sub = forms.CharField(max_length=100)
    # msg = forms.CharField(max_length=100)

    def __str__(self):
        return self.Email



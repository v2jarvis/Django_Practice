from django import forms
from .models import info

class crudform(forms.ModelForm):
    class Meta:
        model=info
        fields='__all__'

# class crudform(forms.Form):
#     name=forms.CharField(max_length=20)
#     email=forms.EmailField()
#     mobile=forms.IntegerField()
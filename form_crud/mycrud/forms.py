from django import forms
from .models import info

class crudform(forms.ModelForm):
    class Meta:
        model=info
        fields='__all__'
        
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be from example.com domain.")
        return cleaned_data
# class crudform(forms.Form):
#     name=forms.CharField(max_length=20)
#     email=forms.EmailField()
#     mobile=forms.IntegerField()
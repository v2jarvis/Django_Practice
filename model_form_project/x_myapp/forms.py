from django import forms

class stud(forms.Form):
    name=forms.CharField(max_length=20)
    mob=forms.IntegerField()
    add=forms.CharField(max_length=20)

    
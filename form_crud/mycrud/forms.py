from django import forms
from .models import info
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class crudform(forms.ModelForm):
    class Meta:
        model=info
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(crudform, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))    
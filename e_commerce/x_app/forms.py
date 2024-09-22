"""
import modules
"""

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserCreationForm, UsernameField)
from django.contrib.auth.models import User

from .models import *


class CustomerRegistrationForm(UserCreationForm):
    """
    This class is used to create a form for customer registration
    """

    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    class Meta:
        """
        This scalten class also know as inner class it is used to
        create a form for customer registration
        """

        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {"email": "Email"}
        widgets = {"username": forms.TextInput(attrs={"class": "form-control"})}


class LoginForm(AuthenticationForm):
    # class LoginForm(forms.Form):
    """
    This class is used to create a form for customer login
    """
    username = UsernameField(
        widget=forms.TimeInput(attrs={"autofocus": True, "class": "form-control"})
    )
    password = forms.CharField(
        label=("password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-control"}
        ),
    )


class MyPasswordChangingForm(PasswordChangeForm):
    """
    This class is used to create a form for password changing
    """

    old_password = forms.CharField(
        label=("Old Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "autofocus": True,
                "class": "form-control",
            }
        ),
    )
    new_password1 = forms.CharField(
        label=("New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("Confirm New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
    )


class CustomerProfileForm(forms.ModelForm):
    """
    This class is used to create a form for customer profile
    """

    class Meta:
        """
        This scalten class also know as inner class it is used to create a form for customer profile
        """

        model = Customer
        fields = ["name", "locality", "city", "state", "pincode"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "locality": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "state": forms.Select(attrs={"class": "form-control"}),
            "pincode": forms.NumberInput(attrs={"class": "form-control"}),
        }

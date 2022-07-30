from django import forms
from account.models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm,
PasswordResetForm, SetPasswordForm)





class CustomUserCreationForm(UserCreationForm):
    # username = forms.CharField(
    #     widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'User Name'}))
    # )
    # email = forms.CharField(
    #     widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : 'Email'})
    # )
    # mobile = forms.IntegerField(
    # widget=forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Mobile'})
    # )
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Password'})
    # )
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Confirm Password'})
    # )


    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'mobile', 'password1', 'password2', 'is_admin_request' )

class CustomLoginForm(AuthenticationForm):
    username = forms.IntegerField(
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Mobile Number'}),
        
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Password'})
    )


class CustomPasswordResetForm(PasswordResetForm):
        email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", "class" : "form-control"}),
    )

class CustomSetPasswordForm(SetPasswordForm):
        new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class" : "form-control"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
        new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class" : "form-control"}),
    )
        

from django import forms
from profiles.models import CustomerAddress
from account.models import CustomUser

class ProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'gender', 'dob', 'profile_pic')

        widgets = { 
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control', }),
            'gender' : forms.Select(attrs={'class' : 'form-control'}),
            'dob' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date' }),
            'profile_pic' : forms.FileInput(attrs={'class' : 'form-control'})


        }


class AddressForm(forms.ModelForm):

    class Meta:
        model = CustomerAddress
        fields = ('name', 'address', 'state', 'pin', 'mob')

        widgets = { 
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'address' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 4}),
            'state' : forms.Select(attrs={'class' : 'form-control'}),
            'pin' : forms.NumberInput(attrs={'class' : 'form-control', }),
            'mob' : forms.NumberInput(attrs={'class' : 'form-control'})


        }
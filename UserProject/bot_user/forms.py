from django import forms
from .models import BotUsers


class LoginForm(forms.ModelForm):

    class Meta:
        model = BotUsers
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'required': 'true'}),
            'password': forms.PasswordInput(attrs={'required': 'true'}),
        }


class SignUpForm(forms.ModelForm):

    class Meta:
        model = BotUsers
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'required': 'true'}),
            'last_name': forms.TextInput(attrs={'required': 'true'}),
            'email': forms.EmailInput(attrs={'required': 'true'}),
            'password': forms.PasswordInput(attrs={'required': 'true'}),
            'sex': forms.RadioSelect(attrs={'required': 'true'}),
        }

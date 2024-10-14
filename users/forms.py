from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'country', 'password1', 'password2']

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)

class SetNewPasswordForm(SetPasswordForm):
    pass







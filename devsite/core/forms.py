from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control password',  # ✅ fixed comma, consistent class name
                'placeholder': '••••••••••••',
                'autocomplete': 'new-password',
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your password',
                'autocomplete': 'new-password',
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ('email',)
        labels = {'email': 'Email'}
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'you@sample.com',
                    'autocomplete': 'email',
                }
            ),
        }


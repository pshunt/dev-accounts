# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# class CustomSignupForm(UserCreationForm):
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(attrs={'placeholder': 'Email address'})
#     )
#     username = forms.CharField(
#         max_length=150,
#         widget=forms.TextInput(attrs={'placeholder': 'Username'})
#     )
#     password1 = forms.CharField(
#         label='Password',
#         widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
#     )
#     password2 = forms.CharField(
#         label='Confirm Password',
#         widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
#     )

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for fieldname, field in self.fields.items():
#             field.widget.attrs.update({
#                 'class': 'form-control',
#                 'autocomplete': 'off'
#             })


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser

# class CustomSignupForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email',)
#         labels = {'email': 'Email address'}
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
#         }



# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser

# class CustomSignupForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email',)
#         labels = {
#             'email': 'Email'
#         }
#         widgets = {
#             'email': forms.EmailInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'you@sample.com'
#                 }
#             ),
#             'password1': forms.PasswordInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': '**********'
#                 }
#             ),
#             'password2': forms.PasswordInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Confirm your password'
#                 }
#             ),
#         }


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomSignupForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control, password',
                'placeholder': '••••••••',
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
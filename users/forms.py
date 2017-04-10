from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        label="用户",
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )

    password = forms.CharField(
        label="口令",
        strip=False,
        widget=forms.PasswordInput,
    )
    #
    # def confirm_login_allowed(self, user):
    #     if not user.is_active or not user.is_validated:
    #         raise forms.ValidationError('There was a problem with your login.', code='invalid_login')
#
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="用户名",
        strip=False,
        widget=forms.TextInput,
        help_text="用户名",

    )
    password1 = forms.CharField(
         label="口令",
         strip=False,
         widget=forms.PasswordInput,
         help_text="字母数字口令",
    )
    password2 = forms.CharField(
        label="口令确认",
        widget=forms.PasswordInput,
        strip=False,
        help_text="相同的口令.",
    )
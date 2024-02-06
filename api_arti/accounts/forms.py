from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import Profile


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  'email']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'birth_date']

# class MyUserCreationForm(forms.ModelForm):
#     password = forms.CharField(label="Пароль", strip=False, required=True, widget=forms.PasswordInput)
#     password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput,
#                                        strip=False)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_confirm = cleaned_data.get("password_confirm")
#         if password and password_confirm and password != password_confirm:
#             raise forms.ValidationError('Пароли не совпадают!')
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']

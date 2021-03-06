from django import forms
from django.core.exceptions import ValidationError

from .models import User, Project, Requests


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(strip=False)
    password2 = forms.CharField(strip=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords don't match")
        return password2

    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        user.save()
        return user

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'category', 'description', 'group_link')


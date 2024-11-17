from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Grievance

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['name', 'product_purchased', 'issue_faced', 'file_upload']
        widgets = {
            'issue_faced': forms.Textarea(attrs={'rows': 5}),
        }    
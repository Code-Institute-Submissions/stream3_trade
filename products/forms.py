from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Product


class addMyProductform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image')

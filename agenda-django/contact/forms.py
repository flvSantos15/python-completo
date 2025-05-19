from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class ContacForm(forms.ModelForm):
  first_name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'placeholder': 'Escreva aqui'
      },
      label='Primeiro nome',
      help_text='Insira o primeiro nome'
    )
  )

  picture = forms.ImageField(
    widget=forms.FileInput(
      attrs={
        'accept': 'image/*'
      }
    )
  )

  class Meta:
    model = models.Contact
    fields = (
      'first_name',
      'last_name',
      'phone',
      'email',
      'description',
      'category',
      'picture'
    )
    # widgets = {
    #   'first_name': forms.TextInput(
    #     attrs={
    #       'class': 'form-control',
    #       'placeholder': 'Escreva aqui'
    #     }
    #   )
    # }

  def clean(self):
    # cleaned_data = super().cleaned_data

    self.add_error(
      'first_name',
      ValidationError('First name is required')
    )

    return super().clean()

  def clean_first_name(self):
    first_name = self.cleaned_data.get('first_name')

    if not first_name:
      raise ValidationError('First name is required')

    return first_name

class RegisterForm(UserCreationForm):
  first_name = forms.CharField(
    required=True,
    min_length=3,
    error_messages={
      'required': 'First name is required',
      'min_length': 'First name must have at least 3 characters'
    }
  )

  last_name = forms.CharField(
    required=True,
    min_length=3,
    error_messages={
      'required': 'Last name is required',
      'min_length': 'Last name must have at least 3 characters'
    }
  )

  email = forms.EmailField(
    required=True,
    error_messages={
      'required': 'Email is required',
      'invalid': 'Email is invalid'
    }
  )

  class Meta:
    model = User
    fields = (
      'first_name', 'last_name', 'email',
      'username', 'password1', 'password2'
    )

  def clean_email(self):
    email = self.cleaned_data.get('email')

    if User.objects.filter(email=email).exists():
      self.add_error(
        'email',
        ValidationError('Email already exists')
      )

    return email


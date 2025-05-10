from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContacForm(forms.ModelForm):
  first_name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'classe-a classe-b',
        'placeholder': 'Escreva aqui'
      },
      label='Primeiro nome',
      help_text='Insira o primeiro nome'
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
from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContacForm(forms.ModelForm):
  class Meta:
    model = models.Contact
    fields = (
      'first_name',
      'last_name',
      'phone'
    )

  def clean(self):
    # cleaned_data = super().cleaned_data

    self.add_error(
      'first_name',
      ValidationError('First name is required')
    )

    return super().clean()
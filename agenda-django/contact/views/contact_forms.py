from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms

class ContacForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = (
      'first_name',
      'last_name',
      'phone'
    )

# Create your views here.
def create(request):
  if request.method == 'POST':
    context = {
      'form': ContacForm(request.POST),
    }

    return render(
      request,
      'contact/create.html',
      context
    )

  context = {
    'form': ContacForm(),
  }

  return render(
    request,
    'contact/create.html',
    context
  )


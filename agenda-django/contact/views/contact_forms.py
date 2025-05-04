from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def create(request):
  if request.method == 'POST':
    pass

  context = {

  }

  return render(
    request,
    'contact/create.html',
    context
  )


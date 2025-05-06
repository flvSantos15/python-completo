from django.shortcuts import render
from contact.forms import ContacForm

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


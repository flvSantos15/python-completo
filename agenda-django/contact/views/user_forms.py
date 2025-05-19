from django.shortcuts import render
from django.contrib import messages
from .forms import RegisterForm

def register(request):
  form = RegisterForm()

  if request.method == 'POST':
    form = RegisterForm(request.POST)

    if form.is_valid():
      form.save()
      messages.success(request, 'User created successfully')
      return redirect('contact:index')

  return render(
    request,
    'contact/register.html',
    {
      'form': form
    }
  )
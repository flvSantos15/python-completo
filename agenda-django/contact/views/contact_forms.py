from django.shortcuts import render, redirect
from contact.forms import ContacForm

# Create your views here.
def create(request):
  if request.method == 'POST':
    form = ContacForm(request.POST)

    

    context = {
      'form': form,
    }

    if form.is_valid():
      form.save()

      return redirect('contact:index')


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


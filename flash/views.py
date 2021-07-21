from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='/accounts/login/')
def register(request):
    if request.method == 'POST':
     form = Registration(request.POST)
     if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')

      messages.success(request,f'Account for {username} created,you can now login')
      return redirect('login')
    else:
      form = Registration()
    return render(request,'registration/registration_form.html',{"form":form})
# type:ignore
from django.shortcuts import render,redirect
from .forms import *
from rest_framework import viewsets
from .serializer import FlashCardSerializer

class flashCardViewSet(viewsets.ModelViewSet)



# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)

# type:ignore
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import flashCard
from rest_framework import viewsets
from .serializer import FlashCardSerializer

class flashCardViewSet(viewsets.ModelViewSet):
    serializer_class = FlashCardSerializer
    queryset = flashCard.objects.all()

@login_required(login_url='/accounts/login/')
def default(request):
    flashcards=flashCard.objects.all()
    context = {
        "flashcards":flashcards,

    }
    return render(request,'home.html',context)
@login_required(login_url='/accounts/login/')
def flashcard(request,id):
    try:
        flashcards = flashCard.objects.get(id=id)
    except Exception as e:
        raise Http404()
    context={
        "flashcards":flashcards,
    }
    return render(request,'post.html',context)

@login_required(login_url='/accounts/login/')
def profile(request,username):
    profile = User.objects.get(username=username)
    
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    flashcards = flashCard.get_profile_flashcards(profile.id)
    
    return render(request, 'users/profile.html',{"profile":profile,"profile_details":profile_details,"flashcards":flashcards}) 

def search_results(request):
    if 'titles' in request.GET and request.GET['titles']:
        search_term = request.GET.get("titles")
        searched_flashcards = flashCard.search_by_flashcards(search_term).all()
        
        message = f'{search_term}'
        
        return render(request,'search.html',{"message":message,"flashcards":searched_flashcards})
    
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message,})
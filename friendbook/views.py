from django.shortcuts import render
from .models import Profile, Friend_Images

# Create your views here.
def welcome(request):
    allimages = Friend_Images.objects.all()
    allprofiles = Profile.objects.all()

    return render(request, 'homepage.html', {"images":allimages})

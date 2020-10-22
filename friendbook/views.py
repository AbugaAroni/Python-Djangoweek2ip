from django.shortcuts import render
from .models import Profile, Friend_Images

# Create your views here.
def welcome(request):
    allimages = Friend_Images.objects.all()
    allprofiles = Profile.objects.all()

    return render(request, 'homepage.html', {"images":allimages})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Blog_Images.search_by_caption(search_term)
        message = f"{search_term}"

        return render(request, 'everything/search.html',{"message":message,"imgs": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searchresult.html',{"message":message})

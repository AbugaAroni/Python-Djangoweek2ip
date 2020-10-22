from django.shortcuts import render
from .models import Profile, Friend_Images
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    allimages = Friend_Images.objects.all()
    allprofiles = Profile.objects.all()

    return render(request, 'homepage.html', {"images":allimages})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Friend_Images.search_by_caption(search_term)
        message = f"{search_term}"

        return render(request, 'searchresult.html',{"message":message,"imgs": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searchresult.html',{"message":message})

@login_required(login_url='/accounts/login/')
def singleimage(request,image_id):
    try:
        imagez = Friend_Images.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'single-picture.html', {"imagez":imagez})

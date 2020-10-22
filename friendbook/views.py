from django.shortcuts import render,redirect
from .models import Profile, Friend_Images
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm, NewImageForm
from django.db.models import Q

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

@login_required(login_url='/accounts/login/')
def profile(request):
#    allimages = Friend_Images.objects.all()
    current_user = request.user
    allimages = Friend_Images.objects.filter(Q(usersubmitter=current_user))
    allprofiles = Profile.objects.all()
#    allprofiles = Profile.objects.filter(Q(username=current_user))

    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            Profilez = form.save(commit=False)
            Profilez.username = current_user
            Profilez.save()
        return render(request, 'accounts/profile.html', {"form": form, "images":allimages, "profiles":allprofiles})

    else:
        form = NewProfileForm()
    return render(request, 'accounts/profile.html', {"form": form, "images":allimages,  "profiles":allprofiles})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.usersubmitter = current_user

            allprofiles = Profile.objects.get(username=current_user)
            image.profile =  allprofiles
            image.save()
        return redirect(profile)

    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def view_user(request, userid):
    current_user=User.objects.get(id=userid)
    allimages = Friend_Images.objects.filter(Q(usersubmitter=current_user))
    profiles = Profile.objects.get(username=current_user)

    return render(request, 'viewuser.html', {"images":allimages,  "profiles":profiles})

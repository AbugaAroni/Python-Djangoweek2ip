from django.contrib import admin
from .models import Profile, Friend_Images, followers
# Register your models here.

admin.site.register(Profile)
admin.site.register(Friend_Images)
admin.site.register(followers)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from tinymce.models import HTMLField
class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    profilephoto = models.ImageField(upload_to = 'images/')
    bio = HTMLField()

    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        Profile.objects.filter(user_name = self.user_name).update(user_name ='rick')

    class Meta:
        ordering = ['username']

from tinymce.models import HTMLField
class Friend_Images(models.Model):
    title = models.CharField(max_length =60)
    i_images = models.ImageField(upload_to = 'images/')
    caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    usersubmitter = models.ForeignKey(User,on_delete=models.CASCADE)
    comments = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self):
        Friend_Images.objects.filter(title = self.title).update(caption ='rick')

    class Meta:
        ordering = ['title']

    @classmethod
    def search_by_caption(cls,search_term):
        result = cls.objects.filter(caption__icontains=search_term)
        return result


class followers(models.Model):
    userfollower = models.ManyToManyField(User, related_name="joy")
    following = models.ManyToManyField(User, related_name="zac")

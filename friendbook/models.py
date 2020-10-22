from django.db import models

# Create your models here.

class Users(models.Model):
    user_name = models.CharField(max_length =30)
    profilephoto = models.ImageField(upload_to = 'images/')
    bio = models.TextField()

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['user_name']

class Blog_Images(models.Model):
    title = models.CharField(max_length =60)
    i_images = models.ImageField(upload_to = 'images/')
    caption = models.TextField()
    locations = models.ForeignKey(Locations, on_delete=models.CASCADE,)

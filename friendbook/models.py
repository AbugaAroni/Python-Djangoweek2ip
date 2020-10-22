from django.db import models

# Create your models here.

class Profile(models.Model):
    user_name = models.CharField(max_length =30)
    profilephoto = models.ImageField(upload_to = 'images/')
    bio = models.TextField()

    def __str__(self):
        return self.user_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        Profile.objects.filter(user_name = self.user_name).update(user_name ='rick')

    class Meta:
        ordering = ['user_name']

class Friend_Images(models.Model):
    title = models.CharField(max_length =60)
    i_images = models.ImageField(upload_to = 'images/')
    caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    comments = models.TextField()
    likes = models.IntegerField()

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

# Generated by Django 3.1.2 on 2020-10-22 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendbook', '0002_friend_images_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend_images',
            old_name='username',
            new_name='usersubmitter',
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-22 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendbook', '0006_auto_20201023_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followers',
            old_name='following',
            new_name='followinguser',
        ),
        migrations.RenameField(
            model_name='followers',
            old_name='userfollower',
            new_name='user',
        ),
    ]

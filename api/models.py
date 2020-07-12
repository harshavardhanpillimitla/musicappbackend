from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)




# class Post(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     name = models.TextField()
#     latitude = models.FloatField()
#     longitutude = models.FloatField()
#     picture = models.ImageField(default="NULL",upload_to='posts_img')


class Song(models.Model):
    song_name = models.TextField()
    def __str__(self):
        return self.song_name


class Userplaylist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    playlist_name= models.TextField()
    def __str__(self):
        return self.playlist_name



class PlaylistAddedsongs(models.Model):
    playlist_name = models.OneToOneField(Userplaylist,on_delete=models.CASCADE,unique=True,null=False)
    playlistsongs = models.ManyToManyField(Song,related_name='playlistsong',blank=True)


class PlaylistPermission(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name="author")
    playlist = models.ForeignKey(Userplaylist,on_delete=models.CASCADE)
    user_permitted = models.ManyToManyField(User,related_name="permissionsgiven",blank=True,null=True)

    


    



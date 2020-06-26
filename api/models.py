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




class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField()
    latitude = models.FloatField()
    longitutude = models.FloatField()
    picture = models.ImageField(default="NULL",upload_to='posts_img')

from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product
from django.conf import settings
from django.contrib.auth.models import UserManager

class User(AbstractUser):
    """ Cette class sert à utiliser AbstractUser pour obtenir tous ce qu'il nous faut pour un utilisateur """
    objects = UserManager()

#class Profile(models.Model):
#    user = models.OneToOneField('auth.User', on_delete=models.cascade)
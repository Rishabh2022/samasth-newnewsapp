from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
# Create your models here.
class signup(AbstractUser):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=20,blank=False,unique=True,null=False,primary_key=True)
    mobile=PhoneField(null=False,blank=False,unique=True)
    email=models.EmailField(max_length=254,null=False,blank=False,unique=True)
    password=models.CharField(max_length=200)


class Bookmark(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(signup, on_delete=models.CASCADE)
    title = models.TextField()
    readmore=models.URLField(max_length=600)
    image=models.URLField(max_length=500)


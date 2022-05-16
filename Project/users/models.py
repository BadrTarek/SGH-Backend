from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

# Create your models here.


class User(AbstractUser ):
    name = models.CharField(max_length=255)

    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    phone = PhoneNumberField(null=False, blank=False, unique=True)

    image = models.ImageField(null= True,blank = True,  upload_to="UsersUploads/" , default = 'UsersUploads/defaultUserImage.png')

    country = CountryField()

    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.name
    

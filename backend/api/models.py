from django.db import models
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from .con import country

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        now = timezone.now()
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            joined_at=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(**{'{}__iexact'.format(self.model.USERNAME_FIELD): username})

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', max_length=255, unique=True)
    name = models.CharField('Name', max_length=255, unique=True)
    is_staff = models.BooleanField('Is staff', default=False)
    is_active = models.BooleanField('Is active', default=True)
    joined_at = models.DateTimeField('Joined at', default=timezone.now)
    BirthDate = models.DateField(null=True)
    gender = models.CharField(max_length=6, choices=[("M","ذكر"),("F","انثى")],default="غير محدد")
    countries = models.CharField(max_length=255, choices=country ,default="غير محدد")
    Mbti = models.CharField(max_length=4,default="XXXX", choices=[(c,c) for c in ['INTJ','ENTJ','INTP','ENTP','INFJ','ENFJ','INFP','ENFP','ISTJ','ESTJ','ISTP','ESTP','ISFJ','ESFJ','ISFP','ESFP']])

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.name)
    def get_full_name(self):
        return self.name
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

# class UserProfile(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     BirthDate = models.DateField(null=True)
#     gender = models.CharField(max_length=6, choices=[("M","Male"),("F","Female")],default="غير محدد")
#     countries = models.CharField(max_length=255, choices=country ,default="غير محدد")
#     Mbti = models.CharField(max_length=4,default=("XXXX","XXXX"), choices=[(c,c) for c in ['INTJ','ENTJ','INTP','ENTB','INFJ','ENFJ','INFP','ENFP','ISTJ','ESTJ','ISTP','ESTP','ISFJ','ESFJ','ISFP','ESFP']])

#     def __str__(self):
#         return str(self.user)

class Essays(models.Model):
    title         = models.CharField(max_length=255)
    context       = models.TextField(default="هنال خطا ما")
    user          = models.ForeignKey(User,related_name="Essays",on_delete=models.CASCADE)
    publishedDate = models.DateTimeField(auto_now_add=True)
    rating        = models.IntegerField(default=0)
    img           = models.TextField(null=True)
    def __str__(self):
        return self.title
    def get_Essay_object(self):
        return self
    
class Tarh(models.Model):
    title         = models.CharField(max_length=255)
    context       = models.TextField(default="nothing")
    user          = models.ForeignKey(User,on_delete=models.CASCADE)
    publishedDate = models.DateTimeField(auto_now_add=True)
    rating        = models.IntegerField(default=0)
    img           = models.TextField(null=True)
    def __str__(self):
        return self.title

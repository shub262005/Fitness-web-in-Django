from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django import forms
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime


# Create your models here.
class Streak(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    last_login_date = models.DateField(default=date.today)

    def __str__(self):
        return f"Streak for {self.user.username}"
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True, default=None)
    image_file = models.FileField(
        upload_to="images/", max_length=250, null=True, default=None
    )

    def __str__(self):
        return self.name


class Excercisepost(models.Model):
    typeexercise = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True, default=None)
    videolink = models.CharField(max_length=250, default=None, null=True)
    thumbnail = models.FileField(
        upload_to="images/", max_length=250, null=True, default=None
    )

    def __str__(self):
        return self.name


# Diet Models


class DietCat(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True, default=None)
    image_file = models.FileField(
        upload_to="images/", max_length=250, null=True, default=None
    )

    def __str__(self):
        return self.name


class DietPosts(models.Model):
    typeName = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True, default=None)
    dietContent = CKEditor5Field(null=True, default=None, config_name="extends")
    diet_image = models.FileField(
        upload_to="images/", max_length=250, null=True, default=None
    )

    def __str__(self):
        return self.name

# type:ignore
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  bio = models.TextField(default='Happy to code. Share since its caring', max_length=500, blank=True)
  photo = CloudinaryField('photo',default='profile.jpg')
  name = models.CharField(max_length=200)

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete()

  def update_profile(self, id, updated_bio):
    profile = Profile.objects.filter(pk=id).update(bio = updated_bio)
    return profile.save_profile()

  @classmethod
  def search_profile(cls, search):
    profile = cls.objects.filter(user__username__icontains=search)
    return profile

  def __str__(self):
    return self.user.username



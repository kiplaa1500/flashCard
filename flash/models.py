# type:ignore
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
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
  def get_by_id(cls,id):
    profile = Profile.objects.get(user = id)
    return profile
  @classmethod
  def filter_by_id(cls,id):
    profile = Profile.objects.filter(user = id).first()
    return profile
  def __str__(self):
    return self.user.username


class flashCard(models.Model):
    profile=models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    title= models.CharField(max_length=30)
    description = HTMLField(max_length=500,default='write a description')
    pub_date=models.DateTimeField(auto_now_add=True)
    image_landing=CloudinaryField()
    
    def save_flashcards(self):
        self.save()

    def delete_flashcards(self):
        self.delete()
            
    @classmethod
    def search_by_flashcards(cls,search_term):
        flashcards=flashCard.objects.filter(title=search_term)
        return flashcards

    @classmethod
    def get_profile_flashcards(cls,profile):
        flashcards=flashCard.objects.filter(profile__id=profile)
        return flashcards

    def __str__(self):
        return self.title



   

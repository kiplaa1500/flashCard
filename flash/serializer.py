# type:ignore
from rest_framework import serializers
from .models import Profile,flashCard

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','profile_photo',) 
        
        
class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = flashCard
        fields = ('title','image_landing','description')
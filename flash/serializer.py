# type:ignore
from rest_framework import serializers
from .models import Profile,flashCard

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','photo','name') 
        
        
class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = flashCard
        fields = ('title','image_landing','description','pub_date')
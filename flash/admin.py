# type:ignore
from django.contrib import admin

from .models import Profile,flashCard
# Register your models here.

admin.site.register(Profile)
admin.site.register(flashCard)

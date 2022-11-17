from django.contrib import admin
from .models import Length, Type, AbilityLevel, Skis
# Register your models here.

admin.site.register(Length)
admin.site.register(AbilityLevel)
admin.site.register(Type)
admin.site.register(Skis)

from django.contrib import admin
from .models import Player
# Register your models here.

class AdminPlayer(admin.ModelAdmin):
    list_display = ("Nome", "Xp", "PosX", "PosY", "PosZ")

admin.site.register(Player)
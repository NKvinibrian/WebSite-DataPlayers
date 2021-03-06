from django.db import models

# Create your models here.


class Player(models.Model):
    Nome = models.CharField(max_length=100, unique=True)
    Xp = models.IntegerField()
    PosX = models.CharField(max_length=100, default="")
    PosY = models.CharField(max_length=100, default="")
    PosZ = models.CharField(max_length=100, default="")
    Helmet = models.CharField(max_length=20, default="")
    Chestplate = models.CharField(max_length=20, default="")
    Leggings = models.CharField(max_length=20, default="")
    Boot = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.Nome

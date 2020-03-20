from django.db import models

# Create your models here.

class Playlist(models.Model):

    image = models.ImageField(upload_to = "images/Playlist")

    titre = models.TextField(max_length = 255)

    description = models.TextField(max_length = 255)

    date = models.CharField(max_length = 50)

    lien = models.CharField(max_length = 150)

    video = models.URLField(max_length = 150)

    status = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_apdate = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = " "
        verbose_name_plural = " "

    def __str__(self):

        return self.titre

class  Couverture(models.Model):
    
    couverture = models.ImageField(upload_to = "images/Couverture")
    artiste = models.CharField(max_length = 120)
    date = models.CharField(max_length = 60)
    music = models.FileField(max_length = 150)

    status = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_apdate = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = " "
        verbose_name_plural = " "

    def __str__(self):

        return self.artiste
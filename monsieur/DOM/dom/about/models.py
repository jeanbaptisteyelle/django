from django.db import models

# Create your models here.
class Presentation(models.Model):
    nom = models.CharField(max_length = 100)
    prenom = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = "images/Presentation")
    description = models.TextField()
    signature = models.ImageField(upload_to = "images/Presentation")
    vidéo_url = models.URLField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Presentation"
        verbose_name = "Presentation"
        
    def __str__(self):

        return self.nom

class SiteInfo(models.Model):
    adresse = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    contact = models.CharField(max_length = 255)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Presentation"
        verbose_name = "Presentation"
        
    def __str__(self):

        return self.email
    
class Reseau(models.Model):

    ICONS = [
        ('facebook', 'fab fa-facebook'),
        ('intagram', 'fab fa-intagram')

    ]
    nom = models.CharField(max_length = 100)
    lien = models.URLField(max_length = 100)
    icon = models.CharField(choices =ICONS, max_length = 255)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Presentation"
        verbose_name = "Presentation"
        
    def __str__(self):

        return self.email
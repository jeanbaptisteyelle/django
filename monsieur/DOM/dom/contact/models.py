from django.db import models
# Create your models here.

class Contact(models.Model):
    
    contact = models.CharField(max_length = 255)
    message = models.TextField()
    nom = models.CharField(max_length = 100)
    email = models.CharField(max_length = 255)
    sujet = models.CharField(max_length = 255)
    status = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_apdate = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = " "
        verbose_name_plural = " "

    def __str__(self):

        return self.contact

class newletter(models.Model):

    email = models.CharField(max_length = 255)
    status = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_apdate = models.DateTimeField(auto_now = True)

    class Meta:
            verbose_name = " "
            verbose_name_plural = " "

    def __str__(self):

            return self.email

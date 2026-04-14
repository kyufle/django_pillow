from django.db import models
from django.contrib.auth.models import AbstractUser

class Llibre(models.Model):
    titol = models.CharField(max_length=100)
    autor = models.CharField(max_length=200)
    resum = models.TextField(null=True, blank=True)
    data_edicio = models.DateField()
    imatge = models.ImageField(upload_to='llibres/', null=True, blank=True)

    def __str__(self):
        return self.titol

class ImatgeLlibre(models.Model):
    llibre = models.ForeignKey(Llibre, on_delete=models.CASCADE, related_name='galeria')
    imatge = models.ImageField(upload_to='llibres/galeria/')
    descripcio = models.CharField(max_length=100, blank=True, null=True)

class Usuari(AbstractUser):
    auth_token = models.CharField(max_length=32, blank=True, null=True)
from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=14)
    celular =models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name

from django.db import models
import re 


# Create your models here.
class User(models.Model):
    USER_CHOICES = (
        ("user", "Usuário"),
        ("admin", "Administrador")
    )
       
    type_user = models.CharField(max_length=20, choices=USER_CHOICES, default='user', null=False, blank=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length= 254, unique=True, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    
    def __str__(self):
        return self.name
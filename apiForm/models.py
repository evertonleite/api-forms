from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_CHOICES = (
        ("user", "Usuário"),
        ("admin", "Administrador")
    )
       
    name = models.CharField(max_length=254, null=False)
    email = models.EmailField(max_length= 254, unique=True, null=False)
    password = models.CharField(max_length=20, null=False)
    type_user = models.CharField(max_length=20, choices=USER_CHOICES, default='user', null=False)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.name
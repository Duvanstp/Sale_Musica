from django.db import models
from django.contrib.auth.models import AbstractUser

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     birth_date = models.DateField(null=True, blank=True)

#     nombre = models.CharField(max_length=200)
#     apellido = models.CharField(max_length=200)
#     correo = models.CharField(max_length=200)
#     # Otros campos adicionales según tus necesidades

#     def __str__(self):
#         return self.user.username

class Usuario(AbstractUser):
    age = models.IntegerField(default=0)
    token = models.CharField(max_length=200,null=True, blank=True, default='')

    # por defecto trae nombre apellido correo y contraseña
    def __str__(self):
        return self.first_name + " " + self.last_name


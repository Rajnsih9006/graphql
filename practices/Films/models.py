

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField


GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
] 

class ExtendUser(AbstractUser):
    email = models.EmailField( max_length=255)
    # username=models.CharField(max_length=200)
    USERNAME_FIELD="username"
    EMAIL_FIELD="email"
    # def __str__(self):
    #     return str(self.id)

class MoviesName(models.Model):
    user_id = models.ForeignKey(ExtendUser, on_delete=CASCADE,default="")
    actor_name=models.CharField(max_length=200)
    movies_name = models.CharField(max_length=200)
    gender=models.CharField(max_length=50,choices=GENDER_CHOICES,default='Male')

    def __str__(self):
        return str(self.id)

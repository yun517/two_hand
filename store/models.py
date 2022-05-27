from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    birth = models.DateField()

    class Mata:
        ordering = ['-username']
    def __str__(self):
        return str(self.user)

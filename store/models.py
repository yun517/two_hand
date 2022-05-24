from django.db import models
from django.urls import reverse


# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=10, null=True)
    email = models.EmailField()
    birth = models.DateField()

    
    class Mata:
        ordering = ['-username']
    def __str__(self):
        return self.email

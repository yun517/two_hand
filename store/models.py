from django.db import models
from django.urls import reverse

# Create your models here.
class Member(models.Model):
    member_name = models.CharField(max_length=10, null=True)
    member_email = models.EmailField()
    member_birth = models.DateField()


    def get_url(self):
        return reverse("member_detail", args=[str(self.id)])

    def __str__(self):
        return self.member_name
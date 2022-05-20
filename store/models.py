from django.db import models
from django.urls import reverse

# Create your models here.
class Good(models.Model):
    good_title = models.CharField(max_length=30)
    good_name = models.CharField(max_length=30, null=True)
    good_price = models.IntegerField()

    def get_url(self):
        return reverse("good_detail", args=[str(self.id)])

    def __str__(self):
        return self.good_title
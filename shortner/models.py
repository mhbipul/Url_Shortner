from django.db import models

# Create your models here.
#mahmudul
#4321Bipul

class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
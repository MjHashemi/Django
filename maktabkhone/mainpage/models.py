from django.db import models

class Post(models.Model):
  text=models.CharField(max_length=480)
# Create your models here.

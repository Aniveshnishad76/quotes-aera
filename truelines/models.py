
from django.db import models

# Create your models here.
from django.db.models import Model


class RegisterTable(Model):
    username=models.CharField(max_length=16)
    mobileno=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=16)

class QuotesPost(Model):
    topic=models.CharField(max_length=50)
    quotes=models.CharField(max_length=500)
    mobileno=models.CharField(max_length=10)
    username=models.CharField(max_length=16)
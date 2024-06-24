from django.db import models

class User(models.Model):
    name = models.CharField(max_length=225)
    phoneNo = models.IntegerField()
    password = models.CharField(max_length=225)
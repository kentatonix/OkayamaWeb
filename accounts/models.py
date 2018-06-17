from django.db import models

class PersonalData(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)
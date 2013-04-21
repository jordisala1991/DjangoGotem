from django.db import models

class Objective(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    sprint = models.IntegerField()

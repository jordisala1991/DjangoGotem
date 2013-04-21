from django.db import models
from django.forms import ModelForm

class Objective(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    sprint = models.IntegerField()

class ObjectiveForm(ModelForm):
    class Meta:
        model = Objective
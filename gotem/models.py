from django.db import models
from django.forms import ModelForm
from django import forms

class Sprint(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.name

class Objective(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sprint = models.ForeignKey(Sprint)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class ObjectiveForm(ModelForm):
    sprint = forms.ModelChoiceField(queryset=Sprint.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Objective
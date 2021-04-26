from django.db import models

# Create your models here.
class Characters(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100, blank=True, default='')
  gender = models.CharField(max_length=10, blank=True, default='')

  class Meta:
    ordering = ['created']
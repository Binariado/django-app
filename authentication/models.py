from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Customer(Group):
    class Meta:
        proxy = True
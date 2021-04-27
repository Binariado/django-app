"""
Create permission groups
Create permissions (read only) to models for a set of groups
"""
import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

GROUPS = ['developers', 'devops', 'qa', 'operators', 'product']

class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'
  def handle(self, *args, **options):
      for group in GROUPS:
        new_group, created = Group.objects.get_or_create(name=group)

      print("Created default group and permissions.")
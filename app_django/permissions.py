from rest_framework.permissions import BasePermission
from rest_framework import serializers
from django.contrib.auth.models import Group

class IsAdministrador(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="administrador").exists()
        
    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name="administrador").exists()

class IsConductor(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="conductor").exists()
        
    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name="conductor").exists()

class IsTecnico(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="tecnico").exists()
        
    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name="tecnico").exists()

def validate_group(gp):
  group = Group.objects.filter(name=gp).first()
  if group:
    return gp
  raise serializers.ValidationError({"role": "Role do not match"})
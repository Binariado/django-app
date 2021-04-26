from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):

  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  
  password = serializers.CharField(
    write_only=True,
    required=True,
    validators=[validate_password],
    min_length=8
  )

  password_confirm = serializers.CharField(
    write_only=True,
    required=True,
  )

  class Meta:
    model = User
    fields = (
      'id',
      'username',
      'password',
      'password_confirm',
      'email',
      'first_name',
      'last_name'
    )
    extra_kwargs = {
      # 'password':{'write_only': True},
    }

  def validate(self, attrs):
    if attrs['password'] != attrs['password_confirm']:
      raise serializers.ValidationError({"password": "Passwords do not match"})

    return attrs

  def create(self, validated_data):
    user = User.objects.create_user(
      username=validated_data['username'], 
      password=validated_data['password'],
      email=validated_data['email'],
      first_name=validated_data['first_name'], 
      last_name =validated_data['last_name']
    )
    return user

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class UserUpdateSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )

  class Meta:
    model = User
    fields = (
      'username',
      'email',
      'first_name',
      'last_name'
    )
  
  def update(self, instance, validated_data):
    user = self.context['request'].user

    if user.pk != instance.pk:
      raise serializers.ValidationError({
        "authorize": "Not authorized"
      })

    instance.username = validated_data.get('username', instance.username)
    instance.email = validated_data.get('email', instance.email)
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    insntance = super().update(instance, validated_data)
    return insntance
from rest_framework import serializers
from .models import Characters


class CharactersSerilizer(serializers.ModelSerializer):
  class Meta:
    model = Characters
    fields = '__all__'
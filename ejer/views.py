from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Characters
from .serializer import CharactersSerilizer

# Create your views here.
class CharactersViews(generics.ListCreateAPIView):
  queryset = Characters.objects.all()
  serializer_class = CharactersSerilizer

  def post(self, request, *args, **kwargs):
    data = {
      'name': request.data.get('name'), 
      'gender': request.data.get('gender'),
    }
    serializer = CharactersSerilizer(data=data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def is_palindromo(text):
  iqual, aux = 0, 0
  for ind in reversed(range(0, len(text))):
    if text[ind].lower() == text[aux].lower():
      iqual += 1
    aux += 1
  if len(text) == iqual:
    return text
  else:
    return False

class Palindromos(generics.GenericAPIView):
  def post(self, request, *args, **kwargs):
    text = request.data.get('text')
    len_text = len(text)
    palindromos = []

    r1 = 15
    r2 = 4
    for x in range(len_text):
      r1 = r1 + 1
      r2 = r2 + 1
      for y in range(r2, r1):
        if is_palindromo(text[x:y]) and len(text[x:y]) > 4:
          palindromos.append(text[x:y])
          if r1 >= len_text:
           break
          

    return Response({
      "palindromos": palindromos,
      "total_palindromos": len(palindromos),
      "len_string": len_text
    }, status=status.HTTP_201_CREATED)

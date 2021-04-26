from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import RegisterSerializer, UserSerializer, UserUpdateSerializer

# Create your views here.
class RegisterUser(generics.GenericAPIView):
  serializer_class = RegisterSerializer
  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "message": "User created successfully",
    }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
  try:

    refresh_token = request.data["refresh"]
    token = RefreshToken(refresh_token)
    token.blacklist()
    return Response({
      "message": "User log out successfully",
    }, status=status.HTTP_205_RESET_CONTENT)
  except Exception as e:
    return Response({
      "message": "Token invalid",
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me_user(request):
  user = request.user
  content = {
      'user': UserSerializer(user).data,
  }
  return Response(content, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request, pk=None):
  user = User.objects.filter(id = pk).first()
  if user:
    return Response({
      'user': UserSerializer(user).data,
    }, status=status.HTTP_200_OK)
  return Response({
      "message": "User not found",
  }, status=status.HTTP_404_NOT_FOUND)


@permission_classes([IsAuthenticated])
class UserUpdate(generics.UpdateAPIView):
  serializer_class = UserUpdateSerializer
  queryset = User.objects.all()

@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def user_detail(request, pk=None):
  user = User.objects.filter(id = pk).first()

  if user:

    if request.method == 'GET':
      return Response({
        'user': UserSerializer(user).data,
      }, status=status.HTTP_200_OK)

    if request.method == 'PUT':
      user_serializer =  UserUpdateSerializer(user, data=request.data)

      if user_serializer.is_valid():
        user_serializer.save()
        return Response({
          'user': user_serializer.data,
        }, status=status.HTTP_200_OK)

      return Response({
        "errors": user_serializer.errors
      }, status=status.HTTP_400_BAD_REQUEST)

  return Response({
      "message": "User not found",
  }, status=status.HTTP_404_NOT_FOUND)

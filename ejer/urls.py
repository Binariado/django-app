from django.urls import include, path
from django.urls import path
from .views import CharactersViews, Palindromos

urlpatterns = [
    path('characters', CharactersViews.as_view()),
    path('palindromos', Palindromos.as_view())
]
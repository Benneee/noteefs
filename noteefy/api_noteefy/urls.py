from django.urls import path
from .views import ListNoteefs, DetailNoteefs

urlpatterns = [
  path('<int:pk>', DetailNoteefs.as_view()),
  path('', ListNoteefs.as_view())
]

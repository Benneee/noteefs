from django.shortcuts import render
from rest_framework import generics

from .models import ApiNoteefy
from .serializers import ApiNoteefySerializer

# Create your views here.

class ListNoteefs(generics.ListAPIView):
  queryset = ApiNoteefy.objects.all()
  serializer_class = ApiNoteefySerializer

class DetailNoteefs(generics.RetrieveAPIView):
  queryset = ApiNoteefy.objects.all()
  serializer_class = ApiNoteefySerializer

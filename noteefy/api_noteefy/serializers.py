from rest_framework import serializers
from .models import ApiNoteefy

class ApiNoteefySerializer(serializers.ModelSerializer):
  class Meta:
    model = ApiNoteefy
    fields = ('id', 'title', 'body', 'created_at')

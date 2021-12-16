from django.db.models import fields
from rest_framework import serializers
from .models import *

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import home_poly


class poly_serializer(ModelSerializer):
    class Meta:
        model = home_poly
        fields = ['id', 'poly_index_001']

from rest_framework import serializers
from .models import product

#create product serializer to serialize.

class productserializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'


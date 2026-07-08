from rest_framework import serializers
from .models import Cart

#create Cartserializer to store the cart items..

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'
        read_only_fields=['user']

    def create(self, validated_data):
        cart, created=Cart.objects.get_or_create(
            user=validated_data['user'],
            product=validated_data['product'],
            defaults={
                'quantity': validated_data.get('quantity', 1)
            }
        )
        if not created:
            cart.quantity += validated_data.get('quantity', 1)
            cart.save()
        return cart

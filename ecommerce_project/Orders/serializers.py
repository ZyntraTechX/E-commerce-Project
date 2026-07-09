from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        read_only_fields=['status']
    
    def validate(self, attrs):
        user=attrs.get('user')
        product=attrs.get('product')
        cart=attrs.get('cart')

        if cart.user !=user:
            raise serializers.ValidationError("This cart doesn't belonmgs to this user.")
        if cart.product !=product:
            raise serializers.ValidationError("Selected product doesn't match the cart product.")
        return attrs

    def create(self, validated_data):
        order, created=Order.objects.get_or_create(
            user=validated_data['user'],
            product=validated_data['product'],
            cart=validated_data['cart'],
            defaults={'quantity': validated_data.get('quantity', 1),
                     'status': 'pending' 
            },
        )
        if not created:
            order.quantity += validated_data.get('quantity', 1)
            order.save()
        return order
        
class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id', 'product', 'cart', 'quantity', 'status']
        read_only_fields=['id', 'status']

    def update(self,instance, validated_data):
        instance.status= 'confirmed'
        instance.save()
        return instance


        


            
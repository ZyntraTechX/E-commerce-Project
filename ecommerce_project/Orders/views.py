# from urllib import request
from django.shortcuts import render
from .serializers import OrderSerializer, CheckoutSerializer
from .models import Order
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class OrderView(generics.ListCreateAPIView):
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class CheckoutView(generics.UpdateAPIView):
    serializer_class=CheckoutSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
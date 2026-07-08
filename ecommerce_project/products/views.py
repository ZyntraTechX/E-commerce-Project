from django.shortcuts import render
from rest_framework import generics
from .models import product
from .serializers import productserializer
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
# Create your views here.






class productcreate(generics.ListCreateAPIView):
    queryset=product.objects.all()
    serializer_class=productserializer
    permission_classes=[IsAuthenticated]


class productdetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin ,generics.GenericAPIView):
    queryset=product.objects.all()
    serializer_class=productserializer
    permission_classes=[IsAuthenticated]

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
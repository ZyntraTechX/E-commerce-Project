from django.shortcuts import render,redirect
from rest_framework import generics
# from rest_framework.views import APIView
from .models import User
from .serializers import Registerserializer
# from django.contrib.auth import authenticate 
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view
from rest_framework import mixins

#create your Api here...


class RegisterView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=Registerserializer
    

class Detailview(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=User.objects.all()
    serializer_class=Registerserializer

    def get(self,request,pk):
        return self.retrieve(request,pk) 
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
    
    

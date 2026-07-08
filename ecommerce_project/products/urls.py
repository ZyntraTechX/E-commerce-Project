from django.urls import path 
from .views import productcreate, productdetail

urlpatterns=[
    path('api/product/', productcreate.as_view()),
    path('api/product/<int:pk>/', productdetail.as_view())
]
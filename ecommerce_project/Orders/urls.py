from django.urls import path 
from . import views

urlpatterns=[
    path('order/', views.OrderView.as_view()),
    path('order/place/<int:pk>/', views.CheckoutView.as_view()),
]
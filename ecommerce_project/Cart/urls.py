from django.urls import path
from .views import CartView,CartDetail

urlpatterns=[
    path('api/cart', CartView.as_view()),
    path('api/cart/<int:pk>/', CartDetail.as_view()),
]
from django.urls import path
from .views import RegisterView, Detailview
urlpatterns=[
    path ('api/user/', RegisterView.as_view()),
    path ('api/user/<int:pk>/', Detailview.as_view()),
]


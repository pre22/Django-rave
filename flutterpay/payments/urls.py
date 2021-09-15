from django.urls import path 
from payments.view import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
]

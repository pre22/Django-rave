from django.urls import path 
from payments.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
]

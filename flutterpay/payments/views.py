# from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

class HomePageView(TemplateView):
    template_name = "payments/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] =  settings.RAVE_PUBLIC_KEY
        return context
    

# from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
import requests
from django.shortcuts import redirect
from django.urls import reverse







class HomePageView(TemplateView):
    template_name = "payments/homepage.html"

    def get_context_data(self, **kwargs):
        SEC_KEY = settings.RAVE_PRIVATE_KEY
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {{ SEC_KEY }}'}
        url = 'https://api.flutterwave.com/v3/transactions/t/verify'
        resp = requests.get(url, headers = headers)


        context = super().get_context_data(**kwargs)
        context["key"] =  settings.RAVE_PUBLIC_KEY
        if resp.status_code == "successful":
            context["redirect_page"] = redirect(reverse("payment_success"))
        else:
            pass
        return context
    
class SuccessPageView(TemplateView):
    template_name = "payments/success.html"
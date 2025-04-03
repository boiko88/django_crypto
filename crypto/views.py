from django.views.generic import TemplateView

import requests


class CryptoPageView(TemplateView):
    template_name: str = "crypto.html"


class HomePageView(TemplateView):
    template_name = 'home.html'

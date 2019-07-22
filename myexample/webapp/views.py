from django.shortcuts import render
from django.contrib.auth.views import LoginView


class WebappLoginView(LoginView):
    template_name = 'registation/login.html'


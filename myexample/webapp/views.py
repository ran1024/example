import requests, json
from smtplib import SMTPException
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.urls import reverse

from .forms import SendmailForm


class RegisterUser(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    
    def form_valid(self, form):
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('sendmail')


class SendMailView(FormView):
    form_class = SendmailForm
    template_name = 'sendmail.html'

    def form_valid(self, form):
        sender = self.request.user.username
        from_email = form.cleaned_data['from_email']
        body = form.cleaned_data['body']
        body += ('\n' + str(_find_user(from_email)))
        status = True
        user = User.objects.filter(is_staff=True).first()
        try:
            user.email_user('Сообщение администратору', body,
                            from_email=from_email,
                            fail_silently=True)
        except SMTPException:
            status = False
        mail = form.save(commit=False)
        mail.sender = sender
        mail.status = status
        mail.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main_page')


class WebappLoginView(LoginView):
    template_name = 'registration/login.html'


class WebappLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'registration/logout.html'


def home(request):
    return render(request, 'home.html')


class ExitView(RedirectView):
    pattern_name = 'logout'


def _find_user(from_email):
    URL = 'http://jsonplaceholder.typicode.com/users'
    try:
        r = requests.get(URL)
    except requests.exceptions.RequestException:
        return ''
    if r.status_code != 200:
        return ''
    else:
        for item in r.json():
            if item['email'] == from_email:
                return json.dumps(item, indent=4)
        return ''

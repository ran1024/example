from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from smtplib import SMTPException
from django.views import View

from .forms import SendmailForm


def register_user(request):
    template = 'registration/register.html'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('sendmail')
    else:
        form = UserCreationForm()
    return render(request, template, {'form': form})


class WebappLoginView(LoginView):
    template_name = 'registration/login.html'


class WebappLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'registration/logout.html'


def home(request):
    return render(request, 'home.html')


@login_required
def main_page(request):
    return render(request, 'main_page.html')


# def sendmail(request):
#     template = 'sendmail.html'
#
#     if request.method == 'POST':
#         form = SendmailForm(request.POST)
#         if form.is_valid():
#             sender = request.user.username
#             from_email = form.cleaned_data['from_email']
#             body = form.cleaned_data['body']
#             status = True
#             user = User.objects.get(username='admin')
#             try:
#                 user.email_user('Сообщение администратору', body,
#                                 from_email=from_email,
#                                 fail_silently=True)
#             except SMTPException:
#                 status = False
#             mail = form.save(commit=False)
#             mail.sender = sender
#             mail.status = status
#             mail.save()
#             return redirect('main_page')
#
#     form = SendmailForm()
#     return render(request, template, {'form': form})


class SendMailView(View):
    form_class = SendmailForm
    template_name = 'sendmail.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            sender = request.user.username
            from_email = form.cleaned_data['from_email']
            body = form.cleaned_data['body']
            status = True
            user = User.objects.get(username='admin')
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
            return redirect('main_page')

        return render(request, self.template_name, {'form': form})

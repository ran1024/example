from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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
            return redirect('main_page')
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


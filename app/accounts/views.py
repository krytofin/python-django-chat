from django.conf import settings
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .forms import LoginForm
from .models import User


def user_login_view(request:HttpRequest):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                if User.objects.filter(username=cleaned_data['username']).exists():
                    user = authenticate(request, username=cleaned_data['username'])
                    if user:
                        login(request, user)
        else:
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form':form})
    else:
        return redirect(settings.LOGIN_REDIRECT_URL)
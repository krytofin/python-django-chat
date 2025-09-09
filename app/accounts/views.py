from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
                    user = authenticate(request, username=cleaned_data['username'], password=cleaned_data['password'])
                    if user:
                        login(request, user)
                        return redirect(settings.LOGIN_REDIRECT_URL)
                    else:
                        form.add_error(None,"Wrong login or password")
                else:
                    form.add_error(None,"Wrong login or password")
        else:
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form':form})
    else:
        return redirect(settings.LOGIN_REDIRECT_URL)
    
    
@login_required
def logout_view(request:HttpRequest):
    logout(request)
    return redirect('accounts:login')
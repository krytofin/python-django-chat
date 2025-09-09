from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render


@login_required
def index_view(request: HttpRequest):
    return render(request, "chat/index.html")

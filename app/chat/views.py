from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import Group


@login_required
def index_view(request: HttpRequest):
    return render(request, "chat/index.html")


@login_required
def private_chat_view(request: HttpRequest, uuid):
    current_user = request.user
    group = Group.objects.filter(uuid=uuid)
    if group.count() > 1 or not group or current_user not in group.first().users.all():
        return redirect('chat:index_view')
    messages = group.first().messages.all()
    return render(request, 'chat/private_chat.html', {'messages': messages})
    

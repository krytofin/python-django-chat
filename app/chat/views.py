from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render

from accounts.models import User


@login_required
def index_view(request: HttpRequest):
    return render(request, "chat/index.html")


@login_required
def private_chat_view(request: HttpRequest, uuid):
    current_user = request.user
    friend = User.objects.filter(uuid=uuid)
    if (friend.count()) > 1 or (not friend) or (friend.first() not in current_user.friends.all()):
        return redirect("chat:index_view")
    return render(request, 'chat/private_chat.html')
    

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'diner/index.html', {})


def login(request):
    pass


@login_required(login_url='/user/login/')
def admin(request):
    return render(request, 'diner/index.html', {})

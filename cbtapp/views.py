from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):

    return render(request, 'cbtapp/index.html')


def taketest(request):

    buttons = list(range(1, 45))

    return render(request, 'cbtapp/taketest.html', {'buttons': buttons})
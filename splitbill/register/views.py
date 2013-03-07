# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'header' : "SplitBill"
    }
    return render(request, 'authenticate/index.html', context)# Create your views here.

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'header' : "SplitBill"
    }
    return render(request, 'authenticate/index.html', context)

def auth(request):
    isValidUser = authenticate(username=request.POST['username'], password=request.POST['password'])
    if isValidUser != None:
        login(request, isValidUser)
        return load_dashboard(request)
    else:
        context = {
            'header' : "SplitBill",
            'error' : 'Username/Password do not match our records.'
        }
        forwardPath = 'authenticate/index.html'
        return render(request, forwardPath, context)

@login_required
def load_dashboard(request):
    context = {
        'header' : "SplitBill",
        'username' : request.user.username
    }
    return render(request, 'authenticate/dashboard.html', context)

@login_required
def testcontent(request):
    context = {
        'header' : "SplitBill",
        'username' : request.user.username
    }
    return render(request, 'authenticate/testpage.html', context)

def log_out(request):
    logout(request)
    return render(request, 'authenticate/index.html')
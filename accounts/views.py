from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import *

class LoginView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        user = authenticate(
            username=request.POST.get('login'),
            password=request.POST.get('password')
        )
        if user is None:
            return redirect("/user/login/")
        login(request, user)
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')
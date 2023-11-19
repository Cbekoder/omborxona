from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views import View
from accounts.models import *


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "bolimlar.html")
        return redirect('/user/login/')

class ClientsUPView(View):
    def get(self, request):
        return render(request, 'client_update.html')

class ClientsView(View):
    def get(self, request):
        content = {
            "omborlar" : Ombor.objects.all()
        }
        return render(request, 'clients.html', content)

    def post(self, request):
        pass


class ProductView(View):
    def get(self, request):
        return render(request, 'products.html')


def product_update(request):
    return render(request, 'product_update.html')


def stats(request):
    return render(request, 'stats.html')

from django.shortcuts import render, redirect
from UBHacking2020.EasyOrder.forms import RestaurantsCode





# Create your views here.

def home(request):
    context= {}
    template= "EasyOrder/home.html"
    return render(request, template, context)

def menu(request):
    context={}
    template= "EasyOrder/menu.html"
    return render(request, template, context)

def checkout(request):
    context={}
    template= "EasyOrder/checkout.html"
    return render(request, template, context)


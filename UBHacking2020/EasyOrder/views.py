from django.shortcuts import render, redirect
from .forms import RestaurantsCode




# Create your views here.

def home(request):
    form = RestaurantsCode(request.POST or None)
    print (form['Code'].value())
    context= {"form":form}
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


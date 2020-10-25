from django.shortcuts import render, redirect
from .forms import RestaurantsCode
from .models import Restaurant , Product,Cart,CartItem
from .forms import Temp
import os
from twilio.rest import Client




# Create your views here.

def home(request):
    form = RestaurantsCode(request.POST or None)
    context= {"form":form}
    template= "EasyOrder/home.html"
    if request.method == 'POST':
        if 'code' in request.POST:
            code = request.POST['code']
            print(code)
            if form.is_valid():
                ResObject =  Restaurant.objects.get(RestaurantCode = code)
                products = Product.objects.filter(Restaurant = ResObject)
                context= {"form":form, "ResObject" : ResObject, "products":products}
                return render(request, "EasyOrder/menu.html", context)




        if "addtocart" in request.POST:
            print(request.POST)
            Temp.append(request.POST["addtocart"])
            print("HELLO")
            print(Temp)



            codes = request.POST['codes']
            ResObject =  Restaurant.objects.get(RestaurantCode = codes)
            products = Product.objects.filter(Restaurant = ResObject)
            context= {"form":form, "ResObject" : ResObject, "products":products}
            return render(request, "EasyOrder/menu.html", context)






        if "checkout" in request.POST:
            print(request.POST)
            codes = request.POST['codes']
            ResObject =  Restaurant.objects.get(RestaurantCode = codes)
            products = Product.objects.filter(Restaurant = ResObject)
            context= {"form":form, "ResObject" : ResObject, "products":products}
            return render(request, "EasyOrder/checkout.html", context)
















    context= {"form":form}

    return render(request, template, context)

def menu(request):
    return render(request, "EasyOrder/checkout.html", context)


def update_cart(request,slug):
    cart = Cart.objects.all()[0]
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    if not product in cart.products.all():
        cart.products.add(product)

    return redirect(request.META['HTTP_REFERER'])



def checkout(request,slug):
    context={}
    template= "EasyOrder/checkout.html"
    return render(request, template, context)






def sendMessage(number, order):
    account_sid = "AC7b4d732d64b3e0e890bec89fdaeb9070"
    auth_token = '4b17ed563afde38cffe8cc781a413c7f'

    client = Client(account_sid, auth_token)

    total = 0
    for item in order:
        total += float(item[1])

    totalString = str(total)

    client.messages.create(from_='+13125844903',
                           to=number,
                           body="Your order has been created. Your total is: $" + totalString)


sendMessage("NUMBER GOES HERE", [["Tempura Bass Buns" , "18.00"], ["Spiced Chicken Empanadas", "8.95"], ["Crispy Herb Fries" , "7.95"]])


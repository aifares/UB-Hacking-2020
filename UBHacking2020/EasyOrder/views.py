from django.shortcuts import render, redirect
from .forms import RestaurantsCode
from .models import Restaurant , Product




# Create your views here.

def home(request):
    print(request.POST)
    form = RestaurantsCode(request.POST or None)

    context= {"form":form}
    template= "EasyOrder/home.html"
    if request.method == 'POST':

        code = request.POST['code']
        print(code)
        if form.is_valid():
            ResObject =  Restaurant.objects.get(RestaurantCode = code)
            products = Product.objects.get(Restaurant = ResObject)
            context= {"form":form, "ResObject" : ResObject, "products":products}




            return render(request, "EasyOrder/menu.html", context)
    else:
        return render(request, template, context)

    context= {"form":form}

    return render(request, template, context)

def menu(request):
    context={}
    template= "EasyOrder/menu.html"
    return render(request, template, context)

def checkout(request):
    context={}
    template= "EasyOrder/checkout.html"
    return render(request, template, context)


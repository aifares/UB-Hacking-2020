from django.shortcuts import render, redirect
from .forms import RestaurantsCode
from .models import Restaurant , Product,Cart,CartItem
from .forms import Temp




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
            codes = request.POST['codes2']
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


from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()






class Restaurant(models.Model):
    RestaurantCode = models.CharField(max_length=100)
    RestaurantName = models.CharField(max_length=100)

    def __str__(self):
        return self.RestaurantName


class Product(models.Model):
    Restaurant = models.ForeignKey(Restaurant,on_delete=models.PROTECT,default=None)
    Price = models.DecimalField(max_digits=5,decimal_places=2,blank=True, null=True)
    Items = models.CharField(max_length=100,blank=True, null=True)
    Description = models.CharField(max_length=1000,blank=True, null=True)
    Image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(null = True,blank = True)

    def __str__(self):
        return "%s, %s, %s" %(self.Items, self.Price, self.Description)

class CartItem(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', null=True, blank=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True)
    line_total = models.DecimalField(default=1000.00, max_digits=1000, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

class Cart(models.Model):
    cart_items = models.ManyToManyField(CartItem,related_name="CARTITEMS")
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    pennies_total = models.DecimalField(max_digits=100000000, decimal_places=0, default=0)
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)






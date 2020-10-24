from django.db import models

class Restaurant(models.Model):
    RestaurantCode = models.CharField(max_length=100)
    RestaurantName = models.CharField(max_length=100)

    def __str__(self):
        return self.RestaurantName


class Product(models.Model):
    Restaurant = models.ForeignKey(Restaurant,on_delete=models.PROTECT,default=None)
    Price = models.DecimalField(max_digits=5,decimal_places=4,blank=True, null=True)
    Items = models.CharField(max_length=100,blank=True, null=True)
    Description = models.CharField(max_length=1000,blank=True, null=True)
    Image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "%s, %s, %s" %(self.Items, self.Price, self.Description)


from django import forms
from django.contrib import messages
from UBHacking2020.EasyOrder import models


class RestaurantsCode(forms.Form):
    Code = forms.CharField(required=False)

    def clean_code(self):
        code = self.cleaned_data.get("Code")
        try:
            models.Restaurant.objects.get(code = models.Restaurant.RestaurantCode)
        except models.Restaurant.DoesNotExist:
            raise forms.ValidationError("Restaurant Does Not Exist")

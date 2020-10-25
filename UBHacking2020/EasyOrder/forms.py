from django import forms
from django.contrib import messages
from .models import Restaurant

Temp = []

class RestaurantsCode(forms.Form):
    Code = forms.CharField(required=False)

    def clean_code(self):
        code = self.cleaned_data.get("Code")
        try:
            Restaurant.objects.get(RestaurantCode = code)
        except Restaurant.DoesNotExist:
            raise forms.ValidationError("Restaurant Does Not Exist")

from django import forms
from django.contrib import messages
from .models import Restaurant


class RestaurantsCode(forms.Form):
    Code = forms.CharField(required=False)

    def clean_code(self):
        code = self.cleaned_data.get("Code")
        try:
            Restaurant.objects.get(code = Restaurant.RestaurantCode)
        except Restaurant.DoesNotExist:
            raise forms.ValidationError("Restaurant Does Not Exist")

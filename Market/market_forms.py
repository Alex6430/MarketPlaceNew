from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from Market.models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('id_product', 'id_category', 'name_product', 'quantity_product', 'price_product')
        # help_texts = {
        #     'username': None,
        #     'password1': None,
        #     'password2': None,
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['id_product'].label = 'артикул'
        self.fields['id_category'].label = 'категория'
        self.fields['name_product'].label = 'название продукта'
        self.fields['quantity_product'].label = 'количество'
        self.fields['price_product'].label = 'цена'

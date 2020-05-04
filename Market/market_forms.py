from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from Market.models import *

class UpdateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name_product', 'quantity_product', 'price_product')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name_product'].label = 'название продукта'
        self.fields['quantity_product'].label = 'количество'
        self.fields['price_product'].label = 'цена'


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name_product', 'quantity_product', 'price_product')
        # help_texts = {
        #     'id_category': "аккумуляторы",
        #     # 'password1': None,
        #     # 'password2': None,
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.fields['id_product'].label = 'артикул'
    #     self.fields['id_category'].label = 'категория'
    #     self.fields['name_product'].label = 'название продукта'
    #     self.fields['quantity_product'].label = 'количество'
    #     self.fields['price_product'].label = 'цена'


class NameCategoryForm(ModelForm):
    class Meta:
        model = NameCategoryProduct
        fields = ('id_category','id_main_category','name_category')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.fields['id_product'].label = 'артикул'
    #     self.fields['name_category'].label = 'категория'
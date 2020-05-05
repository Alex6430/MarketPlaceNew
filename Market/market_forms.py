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

class DataInput(forms.DateInput):
    input_type = 'date'

class UpdateRequestForm(ModelForm):
    class Meta:
        model = Request
        widgets = {'date_delivery' : DataInput()}
        fields = ('date_delivery','address_delivery')
        help_texts = {
            'date_delivery': '2020-05-05',
            'address_delivery': 'забрать из офиса',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_delivery'].label = 'дата'
        self.fields['address_delivery'].label = 'адрес'
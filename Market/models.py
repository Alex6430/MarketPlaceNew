from django.db import models
from django.contrib.auth.models import User


class NameCategoryProduct(models.Model):
    id_category = models.AutoField(db_column='ID_Category', primary_key=True)  # Field name made lowercase.
    id_main_category = models.ForeignKey('self', models.DO_NOTHING, db_column='ID_Main_Category', blank=True, null=True)  # Field name made lowercase.
    name_category = models.CharField(db_column='Name_Category', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Name_Category_Product'


class NameRequest(models.Model):
    id_status = models.AutoField(db_column='ID_Status', primary_key=True)  # Field name made lowercase.
    name_status = models.CharField(db_column='Name_Status', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Name_Request'


class Product(models.Model):
    id_product = models.AutoField(db_column='ID_Product', primary_key=True)  # Field name made lowercase.
    id_category = models.ForeignKey(NameCategoryProduct, models.DO_NOTHING, db_column='ID_Category')  # Field name made lowercase.
    name_product = models.CharField(db_column='Name_Product', max_length=50)  # Field name made lowercase.
    quantity_product = models.IntegerField(db_column='Quantity_Product')  # Field name made lowercase.
    price_product = models.IntegerField(db_column='Price_Product')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Product'


class ProductRequest(models.Model):
    id_product = models.ForeignKey(Product, models.DO_NOTHING, db_column='ID_Product', primary_key=True)  # Field name made lowercase.
    id_request = models.ForeignKey('Request', models.DO_NOTHING, db_column='ID_Request')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Product_Request'
        unique_together = (('id_product', 'id_request'),)


class Request(models.Model):
    id_request = models.AutoField(db_column='ID_Request', primary_key=True)  # Field name made lowercase.
    id_user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    id_status = models.ForeignKey(NameRequest, models.DO_NOTHING, db_column='ID_Status')  # Field name made lowercase.
    price_request = models.IntegerField(db_column='Price_Request')  # Field name made lowercase.
    date_delivery = models.DateField()
    address_delivery = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'Request'
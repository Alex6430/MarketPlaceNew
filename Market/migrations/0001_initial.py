# Generated by Django 2.1.15 on 2020-04-19 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NameCategoryProduct',
            fields=[
                ('id_category', models.AutoField(db_column='ID_Category', primary_key=True, serialize=False)),
                ('name_category', models.CharField(db_column='Name_Category', max_length=50)),
                ('id_main_category', models.ForeignKey(blank=True, db_column='ID_Main_Category', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Market.NameCategoryProduct')),
            ],
            options={
                'db_table': 'Name_Category_Product',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NameRequest',
            fields=[
                ('id_status', models.AutoField(db_column='ID_Status', primary_key=True, serialize=False)),
                ('name_status', models.CharField(db_column='Name_Status', max_length=50)),
            ],
            options={
                'db_table': 'Name_Request',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.AutoField(db_column='ID_Product', primary_key=True, serialize=False)),
                ('name_product', models.CharField(db_column='Name_Product', max_length=50)),
                ('quantity_product', models.IntegerField(db_column='Quantity_Product')),
                ('price_product', models.IntegerField(db_column='Price_Product')),
            ],
            options={
                'db_table': 'Product',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id_request', models.AutoField(db_column='ID_Request', primary_key=True, serialize=False)),
                ('price_request', models.IntegerField(db_column='Price_Request')),
                ('date_delivery', models.DateField()),
                ('address_delivery', models.CharField(max_length=100)),
                ('id_status', models.ForeignKey(db_column='ID_Status', on_delete=django.db.models.deletion.DO_NOTHING, to='Market.NameRequest')),
                ('id_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Request',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductRequest',
            fields=[
                ('id_product', models.ForeignKey(db_column='ID_Product', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Market.Product')),
                ('quantity', models.IntegerField(db_column='Quantity')),
                ('id_request', models.ForeignKey(db_column='ID_Request', on_delete=django.db.models.deletion.DO_NOTHING, to='Market.Request')),
            ],
            options={
                'db_table': 'Product_Request',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='id_category',
            field=models.ForeignKey(db_column='ID_Category', on_delete=django.db.models.deletion.DO_NOTHING, to='Market.NameCategoryProduct'),
        ),
        migrations.AlterUniqueTogether(
            name='productrequest',
            unique_together={('id_product', 'id_request')},
        ),
    ]

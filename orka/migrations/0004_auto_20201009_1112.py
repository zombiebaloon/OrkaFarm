# Generated by Django 3.1.1 on 2020-10-09 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orka', '0003_customer_order_orderitem_product_shippingaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

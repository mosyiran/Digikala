# Generated by Django 5.1.3 on 2024-12-23 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_size_alter_order_date_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 23, 17, 26, 25, 391454)),
        ),
    ]

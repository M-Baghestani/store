# Generated by Django 5.1.6 on 2025-02-12 19:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_order_date_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 2, 12, 23, 17, 3, 679603)),
        ),
    ]

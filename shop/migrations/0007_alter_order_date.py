# Generated by Django 5.1.6 on 2025-02-14 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 2, 14, 20, 8, 17, 79139)),
        ),
    ]

# Generated by Django 3.2.19 on 2024-09-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order_Table', '0004_auto_20240913_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_table',
            name='total_price',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 3.2.19 on 2024-09-09 15:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order_Table', '0002_alter_order_table_shipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_table',
            name='Total_amount',
        ),
        migrations.RemoveField(
            model_name='order_table',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order_table',
            name='products',
        ),
        migrations.RemoveField(
            model_name='order_table',
            name='user',
        ),
        migrations.AddField(
            model_name='order_table',
            name='product_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='order_table',
            name='quantity',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=1), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='order_table',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order_table',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='shipping',
            field=models.IntegerField(default=0),
        ),
    ]

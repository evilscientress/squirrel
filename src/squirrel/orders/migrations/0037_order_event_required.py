# Generated by Django 3.0.5 on 2020-04-24 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0036_product_default_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="event",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="orders",
                to="orders.Event",
            ),
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0007_product_unit_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="unit_price",
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-24 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0038_pillage_stockpile"),
    ]

    operations = [
        migrations.RemoveField(model_name="order", name="unit_price",),
    ]

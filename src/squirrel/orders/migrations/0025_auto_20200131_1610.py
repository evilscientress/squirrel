# Generated by Django 2.2.9 on 2020-01-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0024_auto_20200131_1416"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="unit",
            field=models.CharField(default="Stück", max_length=20),
        ),
    ]

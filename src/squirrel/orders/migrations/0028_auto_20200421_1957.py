# Generated by Django 2.2.12 on 2020-04-21 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0027_auto_20200413_1459"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(default=None, max_length=250, unique=True),
        ),
    ]

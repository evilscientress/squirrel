# Generated by Django 2.2.8 on 2019-12-09 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0017_auto_20191208_2048"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "permissions": [
                    ("request_order", "Can request a order"),
                    ("approve_order", "Can approve a order"),
                    ("receive_order", "Can receive order"),
                    ("complete_order", "Can compelete order"),
                ]
            },
        ),
    ]

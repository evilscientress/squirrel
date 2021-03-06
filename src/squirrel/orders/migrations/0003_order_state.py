# Generated by Django 2.2.6 on 2019-11-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_auto_20191124_2004"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="state",
            field=models.CharField(
                choices=[
                    ("REQ", "Requested"),
                    ("APP", "Approved"),
                    ("DEL", "Delivered"),
                    ("COM", "Completed"),
                ],
                default="REQ",
                max_length=30,
            ),
        ),
    ]

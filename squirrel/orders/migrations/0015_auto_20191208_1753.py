# Generated by Django 2.2.8 on 2019-12-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0014_auto_20191206_0926"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(default=None, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.CharField(default=None, max_length=50, unique=True),
        ),
    ]

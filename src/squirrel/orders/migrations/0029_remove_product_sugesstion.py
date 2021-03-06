# Generated by Django 2.2.10 on 2020-04-24 09:41

from django.db import migrations


def create_and_set_product_for_suggestion(apps, schema_editor):
    """
    If the order has a product_suggestion, we create a new product with the same name and set it as product.
    Then, we remove the product_suggestion field
    """

    order_model = apps.get_model("orders", "order")
    product_model = apps.get_model("orders", "product")

    for order in order_model.objects.all():
        if order.product_suggestion:
            product = product_model.objects.create(name=order.product_suggestion)
            order.product = product
            order.product_suggestion = ""
            order.save()


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0028_auto_20200421_1957"),
    ]

    operations = [
        migrations.RunPython(create_and_set_product_for_suggestion, elidable=True),
        migrations.RemoveField(model_name="order", name="product_suggestion"),
    ]

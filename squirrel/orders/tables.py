from django.db.models import Q
from django_tables2 import Column, TemplateColumn, tables
from orders.models import Order, Product, Team, Vendor


class VendorTable(tables.Table):
    class Meta:
        model = Vendor
        attrs = {"class": "table table-sm"}
        fields = ["name"]

    edit = TemplateColumn(template_name="tables/vendor_button_column.html")


class TeamTable(tables.Table):
    class Meta:
        model = Team
        attrs = {"class": "table table-sm"}
        fields = ["name"]

    edit = TemplateColumn(template_name="tables/team_button_column.html")


class OrderTable(tables.Table):
    class Meta:
        model = Order
        attrs = {"class": "table table-sm"}
        fields = [
            "amount",
            "item",
            "state",
            "event",
            "team",
            "unit_price",
            "price",
        ]

    # The item that is displayed to the user can either be the wish or the configured product
    item = Column(empty_values=())
    edit = TemplateColumn(template_name="tables/order_button_column.html")
    price = Column(empty_values=(), verbose_name="Order sum")

    @staticmethod
    def render_amount(record):

        # A product always has a unit
        if record.product:
            return f"{record.amount} {record.product.unit}"
        else:
            return record.amount

    @staticmethod
    def render_item(record):
        if record.product:
            return record.product
        else:
            return record.product_suggestion

    @staticmethod
    def render_price(record):
        if record.amount and record.unit_price:
            order_sum = record.amount * record.unit_price

            return f"{order_sum} €"
        return "—"

    @staticmethod
    def render_unit_price(value):
        return f"{value} €"


class ProductTable(tables.Table):
    class Meta:
        model = Product
        attrs = {"class": "table table-sm"}
        fields = ["name", "unit", "ordered_amount"]

    edit = TemplateColumn(template_name="tables/product_button_column.html")
    ordered_amount = Column(
        empty_values=(), verbose_name="Ordered amount not yet on site"
    )

    @staticmethod
    def render_ordered_amount(record):
        """We get all orders for our product that are NOT ready to pick up AND NOT completed"""
        orders = Order.objects.filter(
            Q(product=record), ~Q(state="REA"), ~Q(state="COM"),
        )

        return sum(order.amount for order in orders)


class BudgetTable(tables.Table):
    class Meta:
        model = Team
        attrs = {"class": "table table-sm"}
        fields = ["name", "orders_sum"]

    orders_sum = Column(empty_values=(), verbose_name="Orders sum")

    @staticmethod
    def render_orders_sum(record):
        orders = Order.objects.filter(team=record)
        total = sum(order.unit_price * order.amount for order in orders)

        return f"{total} €"

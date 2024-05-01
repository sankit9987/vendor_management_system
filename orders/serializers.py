from rest_framework import serializers
from orders.models import Order


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "order_number",
            "items",
            "delivery_date",
            "order_date",
            "quantity",
            "status",
            "issue_date",
        ]
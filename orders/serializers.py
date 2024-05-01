from rest_framework import serializers
from orders.models import Order


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "vendor",
            "order_number",
            "items",
            "delivery_date",
            "order_date",
            "quantity",
            "status",
            "issue_date",
            "quality_rate",
            "acknowledged_date",
        ]
        read_only_fields = (
            "order_number",
            "delivery_date",
            "order_date",
            "issue_date",
            "acknowledged_date",
        )

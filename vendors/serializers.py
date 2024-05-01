from rest_framework import serializers
from vendors.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "id",
            "name",
            "address",
            "code",
        ]


class VendorPerformanceSeriaizer(serializers.ManyRelatedField):
    class Meta:
        model = Vendor
        fields = [
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
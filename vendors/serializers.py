from rest_framework import serializers
from vendors.models import Vendor, Performance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"

class VendorPerformanceSeriaizer(serializers.ManyRelatedField):
    class Meta:
        model = Performance
        fields = [
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
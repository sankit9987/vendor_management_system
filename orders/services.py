
from django.db.models import Avg, F, ExpressionWrapper, fields


def calculate_average_time_response(vendor_id:int) -> int:
    """funtion to calculate average time response of vendor
    
    Args:
        vendor_id(int): Vendor_id
    
    Return:
        Average time response of vendor
    """
    from orders.models import Order
    return Order.objects.filter(vendor= vendor_id,
        time_difference=ExpressionWrapper(
            F('acknowledged_date') - F('issue_date'),
            output_field=fields.DurationField()
        )
        ).aggregate(
            average_time=Avg('time_difference')
        )['average_time']


def calculate_on_time_delivery(vendor_id):
    from orders.models import Order
    order_queryset = Order.objects.filter(
        vendor=vendor_id, 
        status=Order.OrderStatus.COMPLETED  
    )

    total_order = order_queryset.count()

    total_order_before_delivery_date = order_queryset.filter(
        delivery_date__lte=F("delivery_date"),).count()
    
    if total_order > 0:
        return total_order_before_delivery_date/total_order
    return 0


def calculate_average_quality_rating(vendor_id):
    from orders.models import Order
    return Order.objects.filter(
        vendor=vendor_id, 
        status=Order.OrderStatus.COMPLETED  , 
    ).aggregate(
        average_rating=Avg('quality_rating')
    )['average_rating']
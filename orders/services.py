from django.db.models import Avg, F, ExpressionWrapper, fields


def calculate_average_time_response(
    vendor_id: int,
    Order,
) -> int:
    """funtion to calculate average time response of vendor

    Args:
        vendor_id(int): Vendor_id
        Order(model): Order models instance

    Return:
        Average time response of vendor in seconds
    """

    avearge_response_time = (
        Order.objects.filter(
            vendor=vendor_id,
        )
        .annotate(
            time_difference=ExpressionWrapper(
                F("acknowledged_date") - F("issue_date"),
                output_field=fields.DurationField(),
            ),
        )
        .aggregate(average_time=Avg("time_difference"))["average_time"]
    )
    if avearge_response_time is not None:
        return avearge_response_time.total_seconds() / (60 * 60 * 24)
    return 0


def calculate_on_time_delivery(vendor_id, Order, total_order):
    """funtion to calculate on time delivery of vendor

    Args:
        vendor_id(int): Vendor_id
        Order(model): Order models instance
        total_order(int):total completed order

    Return:
        On time delivery of vendor
    """

    total_order_before_delivery_date = Order.objects.filter(
        delivery_date__lte=F("delivery_date"),
    ).count()

    if total_order > 0:
        return total_order_before_delivery_date / total_order
    return 0


def calculate_average_quality_rating(vendor_id, Order) -> int:
    """funtion to calculate average quality rating of vendor

    Args:
        vendor_id(int): Vendor_id
        Order(model): Order models instance

    Return:
       Average quality rating
    """
    average_rating = Order.objects.filter(
        vendor=vendor_id,
        status=Order.OrderStatus.COMPLETED,
    ).aggregate(
        average_rating=Avg(
            "quality_rate",
        ),
    )[
        "average_rating"
    ]
    if average_rating is not None:
        return average_rating
    return 0


def calculate_fulfilment_rate(vendor_id, Order, order_queryset) -> int:
    """funtion to calculate fulfilment rate of vendor

    Args:
        vendor_id(int): Vendor_id
        Order(model): Order models instance

    Return:
        Fulfilment rate of vendor
    """
    total_successfull_order = order_queryset.count()

    total_order = Order.objects.filter(
        vendor=vendor_id,
    ).count()

    if total_order > 0:
        return total_successfull_order / total_order
    return 0

import datetime

from django.db import models
from django.core.validators import MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
import random
from orders.services import (
    calculate_on_time_delivery,
    calculate_average_quality_rating,
    calculate_average_time_response,
    calculate_fulfilment_rate,
)
from vendor_management_system.mixins import BaseModel
from vendors.models import Performance, Vendor

# Create your models here.


class Order(BaseModel):
    class OrderStatus(models.IntegerChoices):
        PENDING = 1
        COMPLETED = 2
        CANCELED = 3

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.PROTECT,
        db_index=True,
    )
    order_number = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        editable=False,
    )

    items = models.JSONField()

    order_date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    delivery_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    quantity = models.IntegerField(
        validators=[
            MinValueValidator(1),
        ]
    )
    quality_rate = models.FloatField(
        default=0,
        null=True,
        blank=True,
    )

    status = models.PositiveSmallIntegerField(
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
    )
    issue_date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    acknowledged_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs) -> None:
        self.delivery_date = datetime.datetime.now() + datetime.timedelta(
            days=4,
        )
        self.order_number = f"PoNumber-{random.randint(1,999999)}"
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "tbl_orders"


@receiver(
    post_save,
    sender=Order,
)
def update_vendor_performance(sender, instance, **kwargs):
    vendor_id = instance.vendor
    vendor_performance = Performance.objects.filter(
        vendor=vendor_id,
        create_at__month=datetime.datetime.now().month,
    )
    if len(vendor_performance) > 0:
        print("sss")
        vendor_performance = vendor_performance.first()
    else:
        vendor_performance = Performance.objects.create(
            vendor=vendor_id,
            on_time_delivery_rate=0,
            quality_rating_avg=0,
            average_response_time=0,
            fulfillment_rate=0,
        )

    order_queryset = Order.objects.filter(
        vendor=vendor_id,
        status=Order.OrderStatus.COMPLETED,
    )

    if instance.acknowledged_date:
        average_time_response = calculate_average_time_response(
            vendor_id,
            Order,
        )
        instance.vendor.average_response_time = average_time_response
        vendor_performance.average_response_time = average_time_response

    if instance.status == Order.OrderStatus.COMPLETED:
        total_order = order_queryset.count()
        on_time_delivery_rate = calculate_on_time_delivery(
            vendor_id,
            Order,
            total_order,
        )
        instance.vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor_performance.on_time_delivery_rate = on_time_delivery_rate

    if instance.quality_rate > 0:
        quality_rating_avg = calculate_average_quality_rating(
            vendor_id,
            Order,
        )
        instance.vendor.quality_rating_avg = quality_rating_avg
        vendor_performance.quality_rating_avg = quality_rating_avg

    fulfillment_rate = calculate_fulfilment_rate(
        vendor_id,
        Order,
        order_queryset,
    )

    instance.vendor.fulfillment_rate = fulfillment_rate
    vendor_performance.fulfillment_rate = fulfillment_rate
    instance.vendor.save()
    vendor_performance.save()
    return instance

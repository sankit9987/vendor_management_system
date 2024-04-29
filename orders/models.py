from django.db import models

from vendor_management_system.mixins import BaseModel
from vendors.models import Vendor, Performance
from django.core.validators import MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Avg, F, ExpressionWrapper, fields
from orders.services import calculate_on_time_delivery, calculate_average_quality_rating,calculate_average_time_response
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
    issue_date = models.DateTimeField(auto_now_add=True, editable=False,)

    acknowledged_date = models.DateTimeField()

    def save(self, *args, **kwargs) -> None:
        self.order_number = f"PoNumber-{self.id}"
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "tbl_orders"

@receiver(post_save, sender=Order,)
def update_vendor_performance(sender, instance, **kwargs):
    vendor_id = instance.vendor
    vendor_performance = Performance.objects.get(vendor = vendor_id)

    average_time_response = calculate_average_time_response(vendor_id)
    

    on_time_delivery_rate  = calculate_on_time_delivery(vendor_id)
    quality_rating_avg = calculate_average_quality_rating(vendor_id)
    fulfillment_rate = "s"

    vendor_performance.average_response_time =average_time_response
    vendor_performance.on_time_delivery_rate = on_time_delivery_rate
    vendor_performance.quality_rating_avg = quality_rating_avg
    vendor_performance.fulfillment_rate = fulfillment_rate
    vendor_performance.save()
    return instance


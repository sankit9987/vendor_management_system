from django.db import models

from vendor_management_system.mixins import BaseModel

from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


# Create your models here.
class Vendor(BaseModel):
    name = models.CharField(max_length=100)
    contact_number = models.IntegerField(
        validators=[
            MinValueValidator(1000000000),
            MaxValueValidator(9999999999),
        ]
    )
    address = models.TextField()
    code = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
    )
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def save(self, *args, **kwargs) -> None:
        self.code = uuid.uuid4()
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "tbl_vendors"


class Performance(BaseModel):

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.PROTECT,
    )
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    class Meta:
        db_table = "tbl_vendor_performances"

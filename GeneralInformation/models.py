from django.db import models
from datetime import datetime
# Create your models here.

class General_Information(models.Model):
    Inspection_type=models.CharField(max_length=30)
    booking_ref_number=models.CharField(max_length=100,blank=False)
    supplier_info=models.TextField(max_length=200,blank=False)
    inspection_date=models.DateField(blank=False)
    shipment_date=models.DateField(blank=False)
    factory_date=models.BooleanField(default=False)

    def __str__(self):
        return self.supplier_info
from django import forms
from .models import General_Information


class GIForm(forms.ModelForm):
    class Meta:
        model=General_Information
        fields=[
            "Inspection_type",
            "booking_ref_number",
            "supplier_info",
            "inspection_date",
            "shipment_date",
            "factory_date",

        ]
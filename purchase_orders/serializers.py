from rest_framework import serializers
from .models import Vendor, PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    """Serializes Vendor data """

    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    """Serialize PurchaseOrder data """

    class Meta:
        model = PurchaseOrder
        fields = '__all__'

""" imports """
from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    """Serializer for the Vendor model.""" 
    class Meta:
        """Meta class for VendorSerializer."""
        model = Vendor
        fields = '__all__'

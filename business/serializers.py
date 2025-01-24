from rest_framework import serializers
from .models import BusinessInformation

class BusinessInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessInformation
        fields = ('id', 'business_name', 'current_url', 'email', 'location', 'lat_long', 'phone_number', 'trade_type', 'website')
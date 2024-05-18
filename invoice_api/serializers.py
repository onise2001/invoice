from rest_framework import serializers
from .models import Invoice, Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
 
    class Meta:
        model = Invoice
        fields = "__all__"

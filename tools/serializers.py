from tools.models import Tool, Technician, ToolCheckout
from rest_framework import serializers

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = "__all__"

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = "__all__"

class ToolCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolCheckout
        fields = "__all__"


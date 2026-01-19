from rest_framework import serializers
from core.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Customer
        fields = "__all__"

    def validate_email(self, value):
        if Customer.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Customer with this email already exists."
            )
        return value

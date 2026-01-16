from rest_framework import serializers
from core.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    assigned_to = serializers.ReadOnlyField(source="assigned_to.username")

    class Meta:
        model = Lead
        fields = "__all__"

    def validate_email(self, value):
        if Lead.objects.filter(email=value).exists():
            raise serializers.ValidationError("Lead with this email already exists.")
        return value

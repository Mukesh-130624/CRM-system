from rest_framework import serializers
from core.models import Deal
from core.constants.deal_pipeline import DEAL_PIPELINE


class DealSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Deal
        fields = "__all__"


class DealStageSerializer(serializers.Serializer):
    stage = serializers.ChoiceField(choices=[(k, k) for k in DEAL_PIPELINE.keys()])

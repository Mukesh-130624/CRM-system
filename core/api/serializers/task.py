from rest_framework import serializers
from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def validate(self, data):
        links = [
            data.get("customer"),
            data.get("lead"),
            data.get("deal"),
        ]
        if sum(link is not None for link in links) != 1:
            raise serializers.ValidationError(
                "Task must be linked to exactly one: customer, lead, or deal."
            )
        return data

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from core.models import Deal
from core.api.serializers.deal import DealSerializer, DealStageSerializer
from core.api.permissions import IsDealOwnerOrManager
from core.services.deal_service import change_deal_stage
from core.api.serializers.task import TaskSerializer


class DealViewSet(ModelViewSet):
    serializer_class = DealSerializer
    permission_classes = [IsAuthenticated, IsDealOwnerOrManager]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role in ["admin", "manager"]:
            return Deal.objects.all()
        return Deal.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["get"])
    def tasks(self, request, pk=None):
        deal = self.get_object()
        tasks = deal.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def stage(self, request, pk=None):
        deal = self.get_object()
        serializer = DealStageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            change_deal_stage(
                deal=deal,
                new_stage=serializer.validated_data["stage"],
                user=request.user,
            )
        except PermissionError as e:
            return Response({"error": str(e)}, status=status.HTTP_403_FORBIDDEN)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"message": "Deal stage updated successfully"},
            status=status.HTTP_200_OK,
        )

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Lead
from core.api.serializers.lead import LeadSerializer
from core.api.permissions import IsLeadOwnerOrManager
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from core.services.lead_service import convert_lead_to_customer


class LeadViewSet(ModelViewSet):
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated, IsLeadOwnerOrManager]

    filterset_fields = ["status"]
    search_fields = ["name", "email"]
    ordering_fields = ["created_at"]

    def get_queryset(self):
        user = self.request.user
        if user.role in ["admin", "manager"]:
            return Lead.objects.all()
        return Lead.objects.filter(assigned_to=user)

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)

    @action(detail=True, methods=["post"])
    def convert(self, request, pk=None):
        lead = self.get_object()

        try:
            customer = convert_lead_to_customer(lead, request.user)
        except PermissionError as e:
            return Response({"error": str(e)}, status=status.HTTP_403_FORBIDDEN)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"message": "Lead converted successfully", "customer_id": customer.id},
            status=status.HTTP_201_CREATED,
        )

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Customer
from core.api.serializers.customer import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.role in ["admin", "manager"]:
            return Customer.objects.all()

        return Customer.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

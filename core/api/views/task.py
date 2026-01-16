from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Task
from core.api.serializers.task import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from core.services.task_service import complete_task
from rest_framework.views import exception_handler


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Task.objects.filter(assigned_to=self.request.user)

    def get_queryset(self):
        return Task.objects.select_related("assigned_to").filter(
            assigned_to=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        task = self.get_object()
        complete_task(task, request.user)
        return Response({"status": "completed"}, status=200)

    filterset_fields = ["status", "priority"]
    search_fields = ["title", "description"]
    ordering_fields = ["due_date", "created_at"]

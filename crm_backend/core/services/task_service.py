from django.db import transaction
from core.models import Task


@transaction.atomic
def complete_task(task: Task, user):
    if task.assigned_to != user:
        raise PermissionError("You cannot complete this task.")

    task.status = "completed"
    task.save()
    return task

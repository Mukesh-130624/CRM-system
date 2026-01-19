from django.db import transaction
from core.models import Deal
from core.constants.deal_pipeline import DEAL_PIPELINE


@transaction.atomic
def change_deal_stage(deal: Deal, new_stage: str, user):
    # Permission check
    if user.role not in ["admin", "manager"] and deal.owner != user:
        raise PermissionError("You cannot modify this deal")

    allowed_stages = DEAL_PIPELINE.get(deal.stage, [])

    if new_stage not in allowed_stages:
        raise ValueError(
            f"Invalid stage transition from '{deal.stage}' to '{new_stage}'"
        )

    deal.stage = new_stage
    deal.save()

    return deal

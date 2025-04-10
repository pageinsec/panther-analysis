from panther_aws_helpers import aws_rule_context, get_actor_user, lookup_aws_account_name
from panther_core import PantherEvent


def rule(_) -> bool:
    return True


def title(event: PantherEvent) -> str:
    actor = get_actor_user(event)
    aws_account = lookup_aws_account_name(event.get("recipientAccountId"))
    return f"Multiple SSM Sessions Started by {actor} in {aws_account}"


def alert_context(event: PantherEvent) -> dict:
    return aws_rule_context(event)

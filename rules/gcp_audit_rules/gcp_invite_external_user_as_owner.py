from panther_gcp_helpers import gcp_alert_context


def rule(event):
    if event.deep_get("protoPayload", "response", "error"):
        return False

    method = event.deep_get("protoPayload", "methodName", default="METHOD_NOT_FOUND")
    if method != "InsertProjectOwnershipInvite":
        return False

    authenticated = event.deep_get(
        "protoPayload", "authenticationInfo", "principalEmail", default=""
    )
    expected_domain = authenticated.split("@")[-1]

    if event.deep_get("protoPayload", "request", "member", default="MEMBER_NOT_FOUND").endswith(
        f"@{expected_domain}"
    ):
        return False

    return True


def title(event):
    member = event.deep_get("protoPayload", "request", "member", default="<MEMBER_NOT_FOUND>")
    project = event.deep_get("protoPayload", "resourceName", default="<PROJECT_NOT_FOUND>")
    return f"[GCP]: External user [{member}] was invited as owner to project [{project}]"


def alert_context(event):
    return gcp_alert_context(event)

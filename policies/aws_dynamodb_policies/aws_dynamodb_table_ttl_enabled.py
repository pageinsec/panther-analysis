from panther_base_helpers import deep_get
from panther_config_defaults import IN_PCI_SCOPE

# NOTE: Make sure to adjust IN_PCI_SCOPE


def policy(resource):
    if not IN_PCI_SCOPE(resource):
        return True

    if not resource["TimeToLiveDescription"]:
        return False

    return deep_get(resource, "TimeToLiveDescription", "TimeToLiveStatus") == "ENABLED"

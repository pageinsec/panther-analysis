from panther_config_defaults import IN_PCI_SCOPE

# NOTE: Make sure to adjust IN_PCI_SCOPE


def policy(resource):
    if not IN_PCI_SCOPE(resource):
        return True

    # Casting to Bool as this may be None and we cannot return a NoneType
    return bool(resource["SSLPolicies"])

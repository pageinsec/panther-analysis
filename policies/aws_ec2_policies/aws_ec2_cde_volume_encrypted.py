from panther_config_defaults import IN_PCI_SCOPE

# NOTE: Make sure to adjust IN_PCI_SCOPE


def policy(resource):
    # Only check the volumes that are in scope for PCI
    if not IN_PCI_SCOPE(resource):
        return True

    return bool(resource["Encrypted"])

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ClusterProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the cluster provisioning
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    DELETING = "Deleting"
    UPDATING = "Updating"

class ExpressRouteAuthorizationProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the  ExpressRoute Circuit Authorization provisioning
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    UPDATING = "Updating"

class HcxEnterpriseSiteStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the HCX Enterprise Site
    """

    AVAILABLE = "Available"
    CONSUMED = "Consumed"
    DEACTIVATED = "Deactivated"
    DELETED = "Deleted"

class InternetEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Connectivity to internet is enabled or disabled
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class PrivateCloudProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    PENDING = "Pending"
    BUILDING = "Building"
    DELETING = "Deleting"
    UPDATING = "Updating"

class QuotaEnabled(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Host quota is active for current subscription
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class SslEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Protect LDAP communication using SSL certificate (LDAPS)
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class TrialStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Trial status
    """

    TRIAL_AVAILABLE = "TrialAvailable"
    TRIAL_USED = "TrialUsed"
    TRIAL_DISABLED = "TrialDisabled"

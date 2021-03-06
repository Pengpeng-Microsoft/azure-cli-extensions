# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class Status(str, Enum):

    succeeded = "Succeeded"
    launching = "Launching"
    updating = "Updating"
    deleting = "Deleting"
    deleted = "Deleted"
    failed = "Failed"


class UsableStatus(str, Enum):

    yes = "Yes"
    no = "No"
    partial = "Partial"


class ProvisioningStatus(str, Enum):

    succeeded = "Succeeded"
    provider_launching = "ProviderLaunching"
    provider_updating = "ProviderUpdating"
    provider_deleting = "ProviderDeleting"
    provider_provisioning = "ProviderProvisioning"
    failed = "Failed"


class ResourceIdentityType(str, Enum):

    system_assigned = "SystemAssigned"
    none = "None"

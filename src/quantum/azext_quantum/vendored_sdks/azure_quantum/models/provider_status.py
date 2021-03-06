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

from msrest.serialization import Model


class ProviderStatus(Model):
    """Providers status.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Provider id.
    :vartype id: str
    :ivar current_availability: Provider availability. Possible values
     include: 'Available', 'Degraded', 'Unavailable'
    :vartype current_availability: str or
     ~azure.quantum.models.ProviderAvailability
    :ivar targets:
    :vartype targets: list[~azure.quantum.models.TargetStatus]
    """

    _validation = {
        'id': {'readonly': True},
        'current_availability': {'readonly': True},
        'targets': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'current_availability': {'key': 'currentAvailability', 'type': 'str'},
        'targets': {'key': 'targets', 'type': '[TargetStatus]'},
    }

    def __init__(self, **kwargs):
        super(ProviderStatus, self).__init__(**kwargs)
        self.id = None
        self.current_availability = None
        self.targets = None

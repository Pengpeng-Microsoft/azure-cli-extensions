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


class LivyBatchStateInformation(Model):
    """LivyBatchStateInformation.

    :param not_started_at:
    :type not_started_at: datetime
    :param starting_at:
    :type starting_at: datetime
    :param running_at:
    :type running_at: datetime
    :param dead_at:
    :type dead_at: datetime
    :param success_at:
    :type success_at: datetime
    :param killed_at:
    :type killed_at: datetime
    :param recovering_at:
    :type recovering_at: datetime
    :param current_state:
    :type current_state: str
    :param job_creation_request:
    :type job_creation_request: ~azure.synapse.models.LivyRequestBase
    """

    _attribute_map = {
        'not_started_at': {'key': 'notStartedAt', 'type': 'iso-8601'},
        'starting_at': {'key': 'startingAt', 'type': 'iso-8601'},
        'running_at': {'key': 'runningAt', 'type': 'iso-8601'},
        'dead_at': {'key': 'deadAt', 'type': 'iso-8601'},
        'success_at': {'key': 'successAt', 'type': 'iso-8601'},
        'killed_at': {'key': 'killedAt', 'type': 'iso-8601'},
        'recovering_at': {'key': 'recoveringAt', 'type': 'iso-8601'},
        'current_state': {'key': 'currentState', 'type': 'str'},
        'job_creation_request': {'key': 'jobCreationRequest', 'type': 'LivyRequestBase'},
    }

    def __init__(self, **kwargs):
        super(LivyBatchStateInformation, self).__init__(**kwargs)
        self.not_started_at = kwargs.get('not_started_at', None)
        self.starting_at = kwargs.get('starting_at', None)
        self.running_at = kwargs.get('running_at', None)
        self.dead_at = kwargs.get('dead_at', None)
        self.success_at = kwargs.get('success_at', None)
        self.killed_at = kwargs.get('killed_at', None)
        self.recovering_at = kwargs.get('recovering_at', None)
        self.current_state = kwargs.get('current_state', None)
        self.job_creation_request = kwargs.get('job_creation_request', None)
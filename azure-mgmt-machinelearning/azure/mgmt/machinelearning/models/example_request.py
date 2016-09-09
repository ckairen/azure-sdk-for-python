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


class ExampleRequest(Model):
    """Sample input data for the service's input(s).

    :param inputs: Sample input data for the web service's input(s) given as
     an input name to sample input values matrix map.
    :type inputs: dict
    :param global_parameters: Sample input data for the web service's global
     parameters
    :type global_parameters: dict
    """ 

    _attribute_map = {
        'inputs': {'key': 'inputs', 'type': '{list}'},
        'global_parameters': {'key': 'globalParameters', 'type': '{object}'},
    }

    def __init__(self, inputs=None, global_parameters=None):
        self.inputs = inputs
        self.global_parameters = global_parameters

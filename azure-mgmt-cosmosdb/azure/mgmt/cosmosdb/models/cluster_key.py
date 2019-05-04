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


class ClusterKey(Model):
    """Cosmos DB Cassandra table cluster key.

    :param name: Name of the Cosmos DB Cassandra table cluster key
    :type name: str
    :param order_by: Order of the Cosmos DB Cassandra table cluster key, only
     support "Asc" and "Desc"
    :type order_by: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'order_by': {'key': 'orderBy', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ClusterKey, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.order_by = kwargs.get('order_by', None)

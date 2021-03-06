# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_topology_node import TapiTopologyNode  # noqa: F401,E501
from tapi_server import util


class TapiTopologyGetnodedetailsOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, node=None):  # noqa: E501
        """TapiTopologyGetnodedetailsOutput - a model defined in OpenAPI

        :param node: The node of this TapiTopologyGetnodedetailsOutput.  # noqa: E501
        :type node: TapiTopologyNode
        """
        self.openapi_types = {
            'node': TapiTopologyNode
        }

        self.attribute_map = {
            'node': 'node'
        }

        self._node = node

    @classmethod
    def from_dict(cls, dikt) -> 'TapiTopologyGetnodedetailsOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.topology.getnodedetails.Output of this TapiTopologyGetnodedetailsOutput.  # noqa: E501
        :rtype: TapiTopologyGetnodedetailsOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def node(self):
        """Gets the node of this TapiTopologyGetnodedetailsOutput.


        :return: The node of this TapiTopologyGetnodedetailsOutput.
        :rtype: TapiTopologyNode
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this TapiTopologyGetnodedetailsOutput.


        :param node: The node of this TapiTopologyGetnodedetailsOutput.
        :type node: TapiTopologyNode
        """

        self._node = node

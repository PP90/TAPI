# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_topology_topology import TapiTopologyTopology  # noqa: F401,E501
from tapi_server import util


class TapiTopologyGettopologydetailsOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, topology=None):  # noqa: E501
        """TapiTopologyGettopologydetailsOutput - a model defined in OpenAPI

        :param topology: The topology of this TapiTopologyGettopologydetailsOutput.  # noqa: E501
        :type topology: TapiTopologyTopology
        """
        self.openapi_types = {
            'topology': TapiTopologyTopology
        }

        self.attribute_map = {
            'topology': 'topology'
        }

        self._topology = topology

    @classmethod
    def from_dict(cls, dikt) -> 'TapiTopologyGettopologydetailsOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.topology.gettopologydetails.Output of this TapiTopologyGettopologydetailsOutput.  # noqa: E501
        :rtype: TapiTopologyGettopologydetailsOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def topology(self):
        """Gets the topology of this TapiTopologyGettopologydetailsOutput.


        :return: The topology of this TapiTopologyGettopologydetailsOutput.
        :rtype: TapiTopologyTopology
        """
        return self._topology

    @topology.setter
    def topology(self, topology):
        """Sets the topology of this TapiTopologyGettopologydetailsOutput.


        :param topology: The topology of this TapiTopologyGettopologydetailsOutput.
        :type topology: TapiTopologyTopology
        """

        self._topology = topology

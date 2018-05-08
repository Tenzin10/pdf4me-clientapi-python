# coding: utf-8

"""
    DmsApi

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pdf4me.model.convert_to_pdf_action import ConvertToPdfAction  # noqa: F401,E501
from pdf4me.model.document import Document  # noqa: F401,E501
from pdf4me.model.notification import Notification  # noqa: F401,E501


class ConvertToPdf(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'notification': 'Notification',
        'document': 'Document',
        'convert_to_pdf_action': 'ConvertToPdfAction'
    }

    attribute_map = {
        'notification': 'notification',
        'document': 'document',
        'convert_to_pdf_action': 'convertToPdfAction'
    }

    def __init__(self, notification=None, document=None, convert_to_pdf_action=None):  # noqa: E501
        """ConvertToPdf - a model defined in Swagger"""  # noqa: E501

        self._notification = None
        self._document = None
        self._convert_to_pdf_action = None
        self.discriminator = None

        if notification is not None:
            self.notification = notification
        if document is not None:
            self.document = document
        if convert_to_pdf_action is not None:
            self.convert_to_pdf_action = convert_to_pdf_action

    @property
    def notification(self):
        """Gets the notification of this ConvertToPdf.  # noqa: E501

        Set Notification  # noqa: E501

        :return: The notification of this ConvertToPdf.  # noqa: E501
        :rtype: Notification
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this ConvertToPdf.

        Set Notification  # noqa: E501

        :param notification: The notification of this ConvertToPdf.  # noqa: E501
        :type: Notification
        """

        self._notification = notification

    @property
    def document(self):
        """Gets the document of this ConvertToPdf.  # noqa: E501

        Document containing the data  # noqa: E501

        :return: The document of this ConvertToPdf.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this ConvertToPdf.

        Document containing the data  # noqa: E501

        :param document: The document of this ConvertToPdf.  # noqa: E501
        :type: Document
        """

        self._document = document

    @property
    def convert_to_pdf_action(self):
        """Gets the convert_to_pdf_action of this ConvertToPdf.  # noqa: E501

        Conversion configuration  # noqa: E501

        :return: The convert_to_pdf_action of this ConvertToPdf.  # noqa: E501
        :rtype: ConvertToPdfAction
        """
        return self._convert_to_pdf_action

    @convert_to_pdf_action.setter
    def convert_to_pdf_action(self, convert_to_pdf_action):
        """Sets the convert_to_pdf_action of this ConvertToPdf.

        Conversion configuration  # noqa: E501

        :param convert_to_pdf_action: The convert_to_pdf_action of this ConvertToPdf.  # noqa: E501
        :type: ConvertToPdfAction
        """

        self._convert_to_pdf_action = convert_to_pdf_action

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConvertToPdf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

from pdf4me.model.document import Document  # noqa: F401,E501
from pdf4me.model.notification import Notification  # noqa: F401,E501


class RunJobRes(object):
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
        'job_id': 'str',
        'documents': 'list[Document]',
        'notification': 'Notification'
    }

    attribute_map = {
        'job_id': 'jobId',
        'documents': 'documents',
        'notification': 'notification'
    }

    def __init__(self, job_id=None, documents=None, notification=None):  # noqa: E501
        """RunJobRes - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._documents = None
        self._notification = None
        self.discriminator = None

        self.job_id = job_id
        if documents is not None:
            self.documents = documents
        if notification is not None:
            self.notification = notification

    @property
    def job_id(self):
        """Gets the job_id of this RunJobRes.  # noqa: E501


        :return: The job_id of this RunJobRes.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RunJobRes.


        :param job_id: The job_id of this RunJobRes.  # noqa: E501
        :type: str
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def documents(self):
        """Gets the documents of this RunJobRes.  # noqa: E501

        List of Document Result  # noqa: E501

        :return: The documents of this RunJobRes.  # noqa: E501
        :rtype: list[Document]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this RunJobRes.

        List of Document Result  # noqa: E501

        :param documents: The documents of this RunJobRes.  # noqa: E501
        :type: list[Document]
        """

        self._documents = documents

    @property
    def notification(self):
        """Gets the notification of this RunJobRes.  # noqa: E501

        Set Notification  # noqa: E501

        :return: The notification of this RunJobRes.  # noqa: E501
        :rtype: Notification
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this RunJobRes.

        Set Notification  # noqa: E501

        :param notification: The notification of this RunJobRes.  # noqa: E501
        :type: Notification
        """

        self._notification = notification

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
        if not isinstance(other, RunJobRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

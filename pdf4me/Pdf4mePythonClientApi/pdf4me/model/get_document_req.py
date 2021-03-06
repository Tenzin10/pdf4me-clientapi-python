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

from pdf4me.model.user_fingerprint import UserFingerprint  # noqa: F401,E501


class GetDocumentReq(object):
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
        'document_id': 'str',
        'thumbnails_only': 'bool',
        'document_type': 'str',
        'get_notified': 'bool',
        'connection_id': 'str',
        'user_fingerprint': 'UserFingerprint'
    }

    attribute_map = {
        'job_id': 'jobId',
        'document_id': 'documentId',
        'thumbnails_only': 'thumbnailsOnly',
        'document_type': 'documentType',
        'get_notified': 'getNotified',
        'connection_id': 'connectionId',
        'user_fingerprint': 'userFingerprint'
    }

    def __init__(self, job_id=None, document_id=None, thumbnails_only=None, document_type=None, get_notified=None, connection_id=None, user_fingerprint=None):  # noqa: E501
        """GetDocumentReq - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._document_id = None
        self._thumbnails_only = None
        self._document_type = None
        self._get_notified = None
        self._connection_id = None
        self._user_fingerprint = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if document_id is not None:
            self.document_id = document_id
        if thumbnails_only is not None:
            self.thumbnails_only = thumbnails_only
        if document_type is not None:
            self.document_type = document_type
        if get_notified is not None:
            self.get_notified = get_notified
        if connection_id is not None:
            self.connection_id = connection_id
        if user_fingerprint is not None:
            self.user_fingerprint = user_fingerprint

    @property
    def job_id(self):
        """Gets the job_id of this GetDocumentReq.  # noqa: E501


        :return: The job_id of this GetDocumentReq.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this GetDocumentReq.


        :param job_id: The job_id of this GetDocumentReq.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def document_id(self):
        """Gets the document_id of this GetDocumentReq.  # noqa: E501


        :return: The document_id of this GetDocumentReq.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this GetDocumentReq.


        :param document_id: The document_id of this GetDocumentReq.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def thumbnails_only(self):
        """Gets the thumbnails_only of this GetDocumentReq.  # noqa: E501


        :return: The thumbnails_only of this GetDocumentReq.  # noqa: E501
        :rtype: bool
        """
        return self._thumbnails_only

    @thumbnails_only.setter
    def thumbnails_only(self, thumbnails_only):
        """Sets the thumbnails_only of this GetDocumentReq.


        :param thumbnails_only: The thumbnails_only of this GetDocumentReq.  # noqa: E501
        :type: bool
        """

        self._thumbnails_only = thumbnails_only

    @property
    def document_type(self):
        """Gets the document_type of this GetDocumentReq.  # noqa: E501


        :return: The document_type of this GetDocumentReq.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this GetDocumentReq.


        :param document_type: The document_type of this GetDocumentReq.  # noqa: E501
        :type: str
        """

        self._document_type = document_type

    @property
    def get_notified(self):
        """Gets the get_notified of this GetDocumentReq.  # noqa: E501

        Run the action asynchronously, get notified for any status changes.  # noqa: E501

        :return: The get_notified of this GetDocumentReq.  # noqa: E501
        :rtype: bool
        """
        return self._get_notified

    @get_notified.setter
    def get_notified(self, get_notified):
        """Sets the get_notified of this GetDocumentReq.

        Run the action asynchronously, get notified for any status changes.  # noqa: E501

        :param get_notified: The get_notified of this GetDocumentReq.  # noqa: E501
        :type: bool
        """

        self._get_notified = get_notified

    @property
    def connection_id(self):
        """Gets the connection_id of this GetDocumentReq.  # noqa: E501


        :return: The connection_id of this GetDocumentReq.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this GetDocumentReq.


        :param connection_id: The connection_id of this GetDocumentReq.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def user_fingerprint(self):
        """Gets the user_fingerprint of this GetDocumentReq.  # noqa: E501


        :return: The user_fingerprint of this GetDocumentReq.  # noqa: E501
        :rtype: UserFingerprint
        """
        return self._user_fingerprint

    @user_fingerprint.setter
    def user_fingerprint(self, user_fingerprint):
        """Sets the user_fingerprint of this GetDocumentReq.


        :param user_fingerprint: The user_fingerprint of this GetDocumentReq.  # noqa: E501
        :type: UserFingerprint
        """

        self._user_fingerprint = user_fingerprint

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
        if not isinstance(other, GetDocumentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

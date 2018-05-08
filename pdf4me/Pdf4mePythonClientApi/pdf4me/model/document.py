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

from pdf4me.model.doc_log import DocLog  # noqa: F401,E501
from pdf4me.model.doc_metadata import DocMetadata  # noqa: F401,E501
from pdf4me.model.notification import Notification  # noqa: F401,E501
from pdf4me.model.page import Page  # noqa: F401,E501


class Document(object):
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
        'name': 'str',
        'doc_status': 'str',
        'pages': 'list[Page]',
        'doc_data': 'str',
        'doc_metadata': 'DocMetadata',
        'doc_logs': 'list[DocLog]',
        'notification': 'Notification'
    }

    attribute_map = {
        'job_id': 'jobId',
        'document_id': 'documentId',
        'name': 'name',
        'doc_status': 'docStatus',
        'pages': 'pages',
        'doc_data': 'docData',
        'doc_metadata': 'docMetadata',
        'doc_logs': 'docLogs',
        'notification': 'notification'
    }

    def __init__(self, job_id=None, document_id=None, name=None, doc_status=None, pages=None, doc_data=None, doc_metadata=None, doc_logs=None, notification=None):  # noqa: E501
        """Document - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._document_id = None
        self._name = None
        self._doc_status = None
        self._pages = None
        self._doc_data = None
        self._doc_metadata = None
        self._doc_logs = None
        self._notification = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if document_id is not None:
            self.document_id = document_id
        if name is not None:
            self.name = name
        if doc_status is not None:
            self.doc_status = doc_status
        if pages is not None:
            self.pages = pages
        if doc_data is not None:
            self.doc_data = doc_data
        if doc_metadata is not None:
            self.doc_metadata = doc_metadata
        if doc_logs is not None:
            self.doc_logs = doc_logs
        if notification is not None:
            self.notification = notification

    @property
    def job_id(self):
        """Gets the job_id of this Document.  # noqa: E501

        JobId of Documents WorkingSet  # noqa: E501

        :return: The job_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Document.

        JobId of Documents WorkingSet  # noqa: E501

        :param job_id: The job_id of this Document.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def document_id(self):
        """Gets the document_id of this Document.  # noqa: E501

        DocumentId  # noqa: E501

        :return: The document_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Document.

        DocumentId  # noqa: E501

        :param document_id: The document_id of this Document.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def name(self):
        """Gets the name of this Document.  # noqa: E501

        Give filename inlcuding filetype  # noqa: E501

        :return: The name of this Document.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Document.

        Give filename inlcuding filetype  # noqa: E501

        :param name: The name of this Document.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def doc_status(self):
        """Gets the doc_status of this Document.  # noqa: E501

        Returns the Status of the Document  # noqa: E501

        :return: The doc_status of this Document.  # noqa: E501
        :rtype: str
        """
        return self._doc_status

    @doc_status.setter
    def doc_status(self, doc_status):
        """Sets the doc_status of this Document.

        Returns the Status of the Document  # noqa: E501

        :param doc_status: The doc_status of this Document.  # noqa: E501
        :type: str
        """

        self._doc_status = doc_status

    @property
    def pages(self):
        """Gets the pages of this Document.  # noqa: E501

        Description of pages  # noqa: E501

        :return: The pages of this Document.  # noqa: E501
        :rtype: list[Page]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this Document.

        Description of pages  # noqa: E501

        :param pages: The pages of this Document.  # noqa: E501
        :type: list[Page]
        """

        self._pages = pages

    @property
    def doc_data(self):
        """Gets the doc_data of this Document.  # noqa: E501


        :return: The doc_data of this Document.  # noqa: E501
        :rtype: str
        """
        return self._doc_data

    @doc_data.setter
    def doc_data(self, doc_data):
        """Sets the doc_data of this Document.


        :param doc_data: The doc_data of this Document.  # noqa: E501
        :type: str
        """
        if doc_data is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', doc_data):  # noqa: E501
            raise ValueError("Invalid value for `doc_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._doc_data = doc_data

    @property
    def doc_metadata(self):
        """Gets the doc_metadata of this Document.  # noqa: E501


        :return: The doc_metadata of this Document.  # noqa: E501
        :rtype: DocMetadata
        """
        return self._doc_metadata

    @doc_metadata.setter
    def doc_metadata(self, doc_metadata):
        """Sets the doc_metadata of this Document.


        :param doc_metadata: The doc_metadata of this Document.  # noqa: E501
        :type: DocMetadata
        """

        self._doc_metadata = doc_metadata

    @property
    def doc_logs(self):
        """Gets the doc_logs of this Document.  # noqa: E501


        :return: The doc_logs of this Document.  # noqa: E501
        :rtype: list[DocLog]
        """
        return self._doc_logs

    @doc_logs.setter
    def doc_logs(self, doc_logs):
        """Sets the doc_logs of this Document.


        :param doc_logs: The doc_logs of this Document.  # noqa: E501
        :type: list[DocLog]
        """

        self._doc_logs = doc_logs

    @property
    def notification(self):
        """Gets the notification of this Document.  # noqa: E501


        :return: The notification of this Document.  # noqa: E501
        :rtype: Notification
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this Document.


        :param notification: The notification of this Document.  # noqa: E501
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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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
from pdf4me.model.document import Document  # noqa: F401,E501
from pdf4me.model.pricing import Pricing  # noqa: F401,E501


class DropDocumentRes(object):
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
        'document': 'Document',
        'job_id': 'str',
        'document_list': 'list[Document]',
        'doc_logs': 'list[DocLog]',
        'pricing': 'Pricing',
        'success': 'bool',
        'error_msg': 'str',
        'exception': 'object'
    }

    attribute_map = {
        'document': 'document',
        'job_id': 'jobId',
        'document_list': 'documentList',
        'doc_logs': 'docLogs',
        'pricing': 'pricing',
        'success': 'success',
        'error_msg': 'errorMsg',
        'exception': 'exception'
    }

    def __init__(self, document=None, job_id=None, document_list=None, doc_logs=None, pricing=None, success=None, error_msg=None, exception=None):  # noqa: E501
        """DropDocumentRes - a model defined in Swagger"""  # noqa: E501

        self._document = None
        self._job_id = None
        self._document_list = None
        self._doc_logs = None
        self._pricing = None
        self._success = None
        self._error_msg = None
        self._exception = None
        self.discriminator = None

        if document is not None:
            self.document = document
        self.job_id = job_id
        if document_list is not None:
            self.document_list = document_list
        if doc_logs is not None:
            self.doc_logs = doc_logs
        if pricing is not None:
            self.pricing = pricing
        if success is not None:
            self.success = success
        if error_msg is not None:
            self.error_msg = error_msg
        if exception is not None:
            self.exception = exception

    @property
    def document(self):
        """Gets the document of this DropDocumentRes.  # noqa: E501


        :return: The document of this DropDocumentRes.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this DropDocumentRes.


        :param document: The document of this DropDocumentRes.  # noqa: E501
        :type: Document
        """

        self._document = document

    @property
    def job_id(self):
        """Gets the job_id of this DropDocumentRes.  # noqa: E501


        :return: The job_id of this DropDocumentRes.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DropDocumentRes.


        :param job_id: The job_id of this DropDocumentRes.  # noqa: E501
        :type: str
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def document_list(self):
        """Gets the document_list of this DropDocumentRes.  # noqa: E501


        :return: The document_list of this DropDocumentRes.  # noqa: E501
        :rtype: list[Document]
        """
        return self._document_list

    @document_list.setter
    def document_list(self, document_list):
        """Sets the document_list of this DropDocumentRes.


        :param document_list: The document_list of this DropDocumentRes.  # noqa: E501
        :type: list[Document]
        """

        self._document_list = document_list

    @property
    def doc_logs(self):
        """Gets the doc_logs of this DropDocumentRes.  # noqa: E501


        :return: The doc_logs of this DropDocumentRes.  # noqa: E501
        :rtype: list[DocLog]
        """
        return self._doc_logs

    @doc_logs.setter
    def doc_logs(self, doc_logs):
        """Sets the doc_logs of this DropDocumentRes.


        :param doc_logs: The doc_logs of this DropDocumentRes.  # noqa: E501
        :type: list[DocLog]
        """

        self._doc_logs = doc_logs

    @property
    def pricing(self):
        """Gets the pricing of this DropDocumentRes.  # noqa: E501


        :return: The pricing of this DropDocumentRes.  # noqa: E501
        :rtype: Pricing
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this DropDocumentRes.


        :param pricing: The pricing of this DropDocumentRes.  # noqa: E501
        :type: Pricing
        """

        self._pricing = pricing

    @property
    def success(self):
        """Gets the success of this DropDocumentRes.  # noqa: E501


        :return: The success of this DropDocumentRes.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this DropDocumentRes.


        :param success: The success of this DropDocumentRes.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def error_msg(self):
        """Gets the error_msg of this DropDocumentRes.  # noqa: E501


        :return: The error_msg of this DropDocumentRes.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this DropDocumentRes.


        :param error_msg: The error_msg of this DropDocumentRes.  # noqa: E501
        :type: str
        """

        self._error_msg = error_msg

    @property
    def exception(self):
        """Gets the exception of this DropDocumentRes.  # noqa: E501


        :return: The exception of this DropDocumentRes.  # noqa: E501
        :rtype: object
        """
        return self._exception

    @exception.setter
    def exception(self, exception):
        """Sets the exception of this DropDocumentRes.


        :param exception: The exception of this DropDocumentRes.  # noqa: E501
        :type: object
        """

        self._exception = exception

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
        if not isinstance(other, DropDocumentRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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


class Page(object):
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
        'document_id': 'str',
        'page_id': 'str',
        'page_number': 'int',
        'rotate': 'float',
        'thumbnail': 'str',
        'source_document_id': 'str',
        'source_page_number': 'int'
    }

    attribute_map = {
        'document_id': 'documentId',
        'page_id': 'pageId',
        'page_number': 'pageNumber',
        'rotate': 'rotate',
        'thumbnail': 'thumbnail',
        'source_document_id': 'sourceDocumentId',
        'source_page_number': 'sourcePageNumber'
    }

    def __init__(self, document_id=None, page_id=None, page_number=None, rotate=None, thumbnail=None, source_document_id=None, source_page_number=None):  # noqa: E501
        """Page - a model defined in Swagger"""  # noqa: E501

        self._document_id = None
        self._page_id = None
        self._page_number = None
        self._rotate = None
        self._thumbnail = None
        self._source_document_id = None
        self._source_page_number = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        if page_id is not None:
            self.page_id = page_id
        if page_number is not None:
            self.page_number = page_number
        if rotate is not None:
            self.rotate = rotate
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if source_document_id is not None:
            self.source_document_id = source_document_id
        if source_page_number is not None:
            self.source_page_number = source_page_number

    @property
    def document_id(self):
        """Gets the document_id of this Page.  # noqa: E501


        :return: The document_id of this Page.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Page.


        :param document_id: The document_id of this Page.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def page_id(self):
        """Gets the page_id of this Page.  # noqa: E501


        :return: The page_id of this Page.  # noqa: E501
        :rtype: str
        """
        return self._page_id

    @page_id.setter
    def page_id(self, page_id):
        """Sets the page_id of this Page.


        :param page_id: The page_id of this Page.  # noqa: E501
        :type: str
        """

        self._page_id = page_id

    @property
    def page_number(self):
        """Gets the page_number of this Page.  # noqa: E501


        :return: The page_number of this Page.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this Page.


        :param page_number: The page_number of this Page.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def rotate(self):
        """Gets the rotate of this Page.  # noqa: E501


        :return: The rotate of this Page.  # noqa: E501
        :rtype: float
        """
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        """Sets the rotate of this Page.


        :param rotate: The rotate of this Page.  # noqa: E501
        :type: float
        """

        self._rotate = rotate

    @property
    def thumbnail(self):
        """Gets the thumbnail of this Page.  # noqa: E501


        :return: The thumbnail of this Page.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this Page.


        :param thumbnail: The thumbnail of this Page.  # noqa: E501
        :type: str
        """
        if thumbnail is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', thumbnail):  # noqa: E501
            raise ValueError("Invalid value for `thumbnail`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._thumbnail = thumbnail

    @property
    def source_document_id(self):
        """Gets the source_document_id of this Page.  # noqa: E501


        :return: The source_document_id of this Page.  # noqa: E501
        :rtype: str
        """
        return self._source_document_id

    @source_document_id.setter
    def source_document_id(self, source_document_id):
        """Sets the source_document_id of this Page.


        :param source_document_id: The source_document_id of this Page.  # noqa: E501
        :type: str
        """

        self._source_document_id = source_document_id

    @property
    def source_page_number(self):
        """Gets the source_page_number of this Page.  # noqa: E501


        :return: The source_page_number of this Page.  # noqa: E501
        :rtype: int
        """
        return self._source_page_number

    @source_page_number.setter
    def source_page_number(self, source_page_number):
        """Sets the source_page_number of this Page.


        :param source_page_number: The source_page_number of this Page.  # noqa: E501
        :type: int
        """

        self._source_page_number = source_page_number

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
        if not isinstance(other, Page):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

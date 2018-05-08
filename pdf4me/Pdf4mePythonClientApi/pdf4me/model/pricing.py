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


class Pricing(object):
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
        'currency': 'str',
        'total_cost': 'float',
        'page_cnt': 'int',
        'document_cnt': 'int',
        'pricing_type_required': 'str',
        'pricing_type_of_user': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'total_cost': 'totalCost',
        'page_cnt': 'pageCnt',
        'document_cnt': 'documentCnt',
        'pricing_type_required': 'pricingTypeRequired',
        'pricing_type_of_user': 'pricingTypeOfUser'
    }

    def __init__(self, currency=None, total_cost=None, page_cnt=None, document_cnt=None, pricing_type_required=None, pricing_type_of_user=None):  # noqa: E501
        """Pricing - a model defined in Swagger"""  # noqa: E501

        self._currency = None
        self._total_cost = None
        self._page_cnt = None
        self._document_cnt = None
        self._pricing_type_required = None
        self._pricing_type_of_user = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if total_cost is not None:
            self.total_cost = total_cost
        if page_cnt is not None:
            self.page_cnt = page_cnt
        if document_cnt is not None:
            self.document_cnt = document_cnt
        if pricing_type_required is not None:
            self.pricing_type_required = pricing_type_required
        if pricing_type_of_user is not None:
            self.pricing_type_of_user = pricing_type_of_user

    @property
    def currency(self):
        """Gets the currency of this Pricing.  # noqa: E501


        :return: The currency of this Pricing.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Pricing.


        :param currency: The currency of this Pricing.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def total_cost(self):
        """Gets the total_cost of this Pricing.  # noqa: E501


        :return: The total_cost of this Pricing.  # noqa: E501
        :rtype: float
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this Pricing.


        :param total_cost: The total_cost of this Pricing.  # noqa: E501
        :type: float
        """

        self._total_cost = total_cost

    @property
    def page_cnt(self):
        """Gets the page_cnt of this Pricing.  # noqa: E501


        :return: The page_cnt of this Pricing.  # noqa: E501
        :rtype: int
        """
        return self._page_cnt

    @page_cnt.setter
    def page_cnt(self, page_cnt):
        """Sets the page_cnt of this Pricing.


        :param page_cnt: The page_cnt of this Pricing.  # noqa: E501
        :type: int
        """

        self._page_cnt = page_cnt

    @property
    def document_cnt(self):
        """Gets the document_cnt of this Pricing.  # noqa: E501


        :return: The document_cnt of this Pricing.  # noqa: E501
        :rtype: int
        """
        return self._document_cnt

    @document_cnt.setter
    def document_cnt(self, document_cnt):
        """Sets the document_cnt of this Pricing.


        :param document_cnt: The document_cnt of this Pricing.  # noqa: E501
        :type: int
        """

        self._document_cnt = document_cnt

    @property
    def pricing_type_required(self):
        """Gets the pricing_type_required of this Pricing.  # noqa: E501


        :return: The pricing_type_required of this Pricing.  # noqa: E501
        :rtype: str
        """
        return self._pricing_type_required

    @pricing_type_required.setter
    def pricing_type_required(self, pricing_type_required):
        """Sets the pricing_type_required of this Pricing.


        :param pricing_type_required: The pricing_type_required of this Pricing.  # noqa: E501
        :type: str
        """
        allowed_values = ["free", "basic", "premium", "enterprise"]  # noqa: E501
        if pricing_type_required not in allowed_values:
            raise ValueError(
                "Invalid value for `pricing_type_required` ({0}), must be one of {1}"  # noqa: E501
                .format(pricing_type_required, allowed_values)
            )

        self._pricing_type_required = pricing_type_required

    @property
    def pricing_type_of_user(self):
        """Gets the pricing_type_of_user of this Pricing.  # noqa: E501


        :return: The pricing_type_of_user of this Pricing.  # noqa: E501
        :rtype: str
        """
        return self._pricing_type_of_user

    @pricing_type_of_user.setter
    def pricing_type_of_user(self, pricing_type_of_user):
        """Sets the pricing_type_of_user of this Pricing.


        :param pricing_type_of_user: The pricing_type_of_user of this Pricing.  # noqa: E501
        :type: str
        """
        allowed_values = ["free", "basic", "premium", "enterprise"]  # noqa: E501
        if pricing_type_of_user not in allowed_values:
            raise ValueError(
                "Invalid value for `pricing_type_of_user` ({0}), must be one of {1}"  # noqa: E501
                .format(pricing_type_of_user, allowed_values)
            )

        self._pricing_type_of_user = pricing_type_of_user

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
        if not isinstance(other, Pricing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Here we define classes representing different kinds of strings
that we can find on the web and that we can compare.
"""

import smart_scraper.similarity.strategy as strategy

from bs4 import BeautifulSoup
import lxml.etree


class WebString:
    """
    Base Class representing any string related to a HTML document.

    Attributes:
        _format_name (str): the type of the string wrapped by the class.
            This attribute should be redefined in every child class.
            Each name should be unique.
    """

    _format_name = "web_string"

    def __init__(
            self,
            value: str,
            comparison_strategy: strategy.ComparisonStrategy):
        """
        Args:
            value (str): the string to wrap
            comparison_strategy (strategy.ComparisonStrategy): a class
                that should implement a comparison strategy for the
                value argument.
        """
        self.value = value
        self._comparison_strategy = comparison_strategy

    def compare(self, right: 'WebString') -> float:
        """
        Args:
            right (WebString): an object of this class with which
                the current object should be compared by using the
                comparison strategy given as argument during
                this object's instantiation.

        Returns:
            float: a similarity measure between 0 and 1 given
                by the comparison strategy.

        Raises:
            ValueError: if the current object does not contain a valid
                string in the self.value attribute. This is checked
                via the self.validate method.
        """
        is_valid = self.validate()
        if not is_valid:
            raise ValueError(
                f"value must be of {self._format} format"
            )
        return self._comparison_strategy.compare(
            self.value,
            right.value
        )

    def validate(self) -> bool:
        """
        Returns:
            bool: True if the value attribute is compatible
                with the current class definition; False otherwise.
        Raises:
            NotImplementedError: if an object of this class is used directly.
                This class is intended to be subclassed.
        """
        raise NotImplementedError(
            "This class needs to implement a validate method"
        )


class HTMLString(WebString):
    """
    Class representing an HTML text document

    Attributes:
        _format_name (str): the type of the string wrapped by the class.
            Each name should be unique.
    """
    _format_name = "html_string"
    def __init__(self,
            value: str,
            comparison_strategy: strategy.ComparisonStrategy
            ):
        """
        Args:
            value (str): the string to wrap
            comparison_strategy (strategy.ComparisonStrategy): a class
                that should implement a comparison strategy for the
                value argument.
        """
        super(HTMLString, self).__init__(
            value, comparison_strategy
        )
    
    def validate(self) -> bool:
        """
        Returns:
            bool: True if the value attribute is a
                valid HTML document; False otherwise.
        """
        is_valid = bool(BeautifulSoup(self.value, "html.parser").find())
        return is_valid


class XPathString(WebString):
    """
    Class representing an XPath string

    Attributes:
        _format_name (str): the type of the string wrapped by the class.
            Each name should be unique.
    """
    _format_name = "xpath_string"

    def __init__(
            self,
            value: str,
            comparison_strategy: strategy.ComparisonStrategy
            ):
        """
        Args:
            value (str): the string to wrap
            comparison_strategy (strategy.ComparisonStrategy): a class
                that should implement a comparison strategy for the
                value argument.
        """
        super(XPathString, self).__init__(
            value, comparison_strategy
        )

    def validate(self) -> bool:
        """
        Returns:
            bool: True if the value attribute is a
                valid XPath string; False otherwise.
        """
        try:
            lxml.etree.XPath(self.value)
        except lxml.etree.XPathSyntaxError:
            is_valid = False
        else:
            is_valid = True
        return is_valid

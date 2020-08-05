#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Here we define classes that implement different comparison strategies
between strings
"""

from difflib import SequenceMatcher
import abc


class ComparisonStrategy:
    """
    Abstract class for all comparison strategies
    related to Web Strings
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def compare(self):
        """Required Method"""
        pass

class LevenshteinStrategy(ComparisonStrategy):
    """
    Comparison strategy that uses the levenshtein distance
    """
    def compare(self, left: str, right: str) -> float:
        """
        Args:
            left (str): left string to compare
            right (str): right string to compare
        Returns:
            float: a number between 0 and 1 that
                indicates how similar both strings are
        """
        return SequenceMatcher(None, left, right).ratio()

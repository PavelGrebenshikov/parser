# For imports
import os
import sys
sys.path.append(os.path.abspath('../classes'))
sys.path.append(os.path.abspath('../config'))

from settings import URL, HEADER

# import classes for unit tests
from class_parser import ClassParser
from class_strings import ClassViewContent
from class_template import ClassViewTemplate

# import unit test
from unittest import TestCase

# Create to class TestCase
class TestCaseParser(TestCase):

    # First test function check_access
    def test_check_access(self):
        my_bools = True
        response = ClassParser.check_access(self, URL, HEADER)
        self.assertEqual(my_bools, response[0])
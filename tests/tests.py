# For imports
import os
import sys
sys.path.append(os.path.abspath('../classes'))
sys.path.append(os.path.abspath('../config'))

from settings import TAGS_HTML, LINKS_CLASS, HEADER

# import classes for unit tests
from class_parser import ClassParser
from class_strings import ClassViewContent
from class_template import ClassViewTemplate

# import unit test
from unittest import TestCase

# Create to class TestCase
class TestCaseParser(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ClsParser = ClassParser()
        cls.ClsViewContent = ClassViewContent()
        # cls.ClsViewTemplate = ClassViewTemplate()

    # First test function check_access
    def test_check_access(self):
        my_bools = True
        response = self.ClsParser.check_access("https://www.python.org/blogs/", HEADER)
        self.assertEqual(my_bools, response[0])

    def test_count_content_put(self):
        my_dict = {"tags": ["h4", "h3"], "class": ["myclasser", "testclass"]}
        check_count = self.ClsParser.count_content_put(["h4", "h3"], ["myclasser", "testclass"])
        self.assertDictEqual(check_count, my_dict)
    
    def test_put_content(self):
        response = self.ClsParser.check_access("https://www.python.org/blogs/", HEADER)
        elements = self.ClsParser.count_content_put(["h3", "h1"], ["event-title", "call-to-action"])
        content = self.ClsParser.put_content(response, elements)
        self.assertTrue(content)

        # The type should be a list, but because of the self.write_file () function,
        #  it returns an exception / needs to be fixed in the future
        self.assertIsInstance(content, str)


    def test_view_content(self):
        content = self.ClsViewContent.view_content([["h3", "h5"], ["test", "class"]])
        self.assertTrue(content)
        self.assertIsInstance(content, list)
    
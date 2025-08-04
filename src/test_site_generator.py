import unittest
from site_generator import extract_title

class TestSiteGenerator(unittest.TestCase):
    def test_extact_title(self):
        markdown = """
### Some content
# Title here  
            """
        title = extract_title(markdown)
        self.assertEqual(title, "Title here")

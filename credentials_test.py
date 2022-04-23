import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    """
    Test class that defines test case for User class behaviors

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test case
        """
        self.new_user = Credential("Clinton","comPlex!")

    def tearDown(self):
        """
        tearDown method cleans up after each test case
        """
        Credential.credential_list = []

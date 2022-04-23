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
        self.new_credential = Credential("twitter","pass123","john.doe@ymail")

    def tearDown(self):
        """
        tearDown method cleans up after each test case
        """
        Credential.credential_list = []

    def test_init(self):
        """
        test_init test case to test if object is intialized properly
        """

        self.assertEqual(self.new_credential.name,"twitter")
        self.assertEqual(self.new_credential.password, "pass123")
        self.assertEqual(self.new_credential.email, "john.doe@ymail")


if __name__ == "__main__":
    unittest.main()
import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test case for User class behaviors

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test case
        """
        self.new_user = User("Clinton","comPlex!")

    def test_init(self):
        """
        test_init test case to test if object is intialized properly
        """

        self.assertEqual(self.new_user.username,"Clinton")
        self.assertEqual(self.new_user.password, "comPlex!")

if __name__ == "__main__":
    unittest.main()

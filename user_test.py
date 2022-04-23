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

    def test_save_user(self):
        """
        test_save_user test case checks if user object is saved in user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

if __name__ == "__main__":
    unittest.main()

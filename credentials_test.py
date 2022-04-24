import unittest
import pyperclip
from credentials import Credential

class TestCredential(unittest.TestCase):
    """
    Test class that defines test case for credential class behaviors

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
        Credential.credentials_list = []

    def test_init(self):
        """
        test_init test case to test if object is intialized properly
        """

        self.assertEqual(self.new_credential.name,"twitter")
        self.assertEqual(self.new_credential.password, "pass123")
        self.assertEqual(self.new_credential.email, "john.doe@ymail")

    def test_save_credential(self):
        """
        test_save_credential test case checks if credential object is saved in credential list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),1)

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","pass")
            test_credential.save_credential()
            self.assertEqual(len(Credential.credentials_list),2)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credentials_list)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","user","pass")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credentials_list),1)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test3","user","pass")
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Test3")

        self.assertTrue(credential_exists)

    def test_copy_credential(self):
        '''
        Test to confirm that we are copying the credential from a found credential
        '''

        self.new_credential.save_credential()
        Credential.copy_credential("twitter")

        self.assertEqual(self.new_credential,pyperclip.paste())



if __name__ == "__main__":
    unittest.main()
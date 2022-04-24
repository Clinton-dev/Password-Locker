import pyperclip
from password_generator import PasswordGenerator


class Credential:
    """
    Class that generates new instances of credentials
    """

    credentials_list = []

    def __init__(self,name, username, password, email):
        """
        __init__ method defines property of credentail object

        Arg:
            username: new credential name
            password: new credentail password
            email: new credential email
        """

        self.name = name
        self.username = username
        self.password = password
        self.email = email

    def save_credential(self):
        """
        save_credential saves credential in credential list
        """
        Credential.credentials_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method deletes a saved credentail from the credentials_list
        '''
        Credential.credentials_list.remove(self)

    def gen_rand_pass(self):
        """
        generate random password for user credential
        """
        password = PasswordGenerator()
        password.generate()
        return password


    @classmethod
    def display_credentials(cls):
        '''
        method that returns a list of all credentials saved
        '''
        return cls.credentials_list

    @classmethod
    def credential_exist(cls,name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            name: name of credential to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credentials_list:
            if credential.name == name:
                    return True

        return False

    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a credentail that matches that name.

        Args:
            name: name of the credential to search for
        Returns :
            Credential of user that matches the name.
        '''

        for credential in cls.credentials_list:
            if credential.name == name:
                return credential

    @classmethod
    def copy_credential(cls,name):
        contact_found = Credential.find_by_name(name)
        pyperclip.copy(contact_found.name)


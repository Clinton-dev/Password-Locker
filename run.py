#!/usr/bin/env python3.8
from user import User
from credentials import Credential
from user import User

def create_user(username,password):
    '''
    Function to create a new user account
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save contact
    '''
    user.save_contact()

def del_user(user):
    '''
    Function to delete a contact
    '''
    user.delete_user()

def check_existing_user(name):
    '''
    Function that check if a credential exists with that name and return a Boolean
    '''
    return User.user_exist(name)


def create_credential(name, username, password, email):
    '''
    Function to create a credential
    '''
    new_credential = Credential(name, username, password, email)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_contact()

def find_credential(name):
    '''
    Function that finds a credential by credential and returns the credential
    '''
    return Credential.find_by_name(name)

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_credential()

def check_existing_credential(name):
    '''
    Function that check if a credential exists with that name and return a Boolean
    '''
    return Credential.credential_exist(name)


def main():
    print("Hello Welcome to your password Locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user account, dc - display credentials, fc -find a credentials, ex -exit the application ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New User account")
            print("-"*10)

            print ("username ....")
            username = input()

            print("password...")
            password = input()

            save_user(create_user(username,password))
            print ('\n')
            print(f"New user {username} was created!!")
            print ('\n')
        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your contacts")
                print('\n')

                for credentials in display_credentials():
                        print(f"{credentials.name} {credentials.username} {credentials.password} .....{credentials.email}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the name you want to search for")

            search_name = input()
            if check_existing_credential(search_name):
                    search_credential = find_credential(search_name)
                    print(f"Credential name {search_credential.name}")
                    print('-' * 20)

                    print(f"Username .......{search_credential.username}")
                    print(f"password .......{search_credential.password}")
                    print(f"Email address.......{search_credential.email}")
            else:
                    print("That contact does not exist")

        elif short_code == "ex":
                print("Adios .......")
                break
        else:
            print("Please use the short codes")




if __name__ == '__main__':
    main()
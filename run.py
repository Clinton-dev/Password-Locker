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
    user.save_user()

def check_existing_user(name):
    '''
    Function that check if a credential exists with that name and return a Boolean
    '''
    return User.user_exist(name)


def create_credential(name, username, password, email,creator):
    '''
    Function to create a credential
    '''
    new_credential = Credential(name, username, password, email,creator)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

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
    return Credential.display_credentials()

def check_existing_credential(name):
    '''
    Function that check if a credential exists with that name and return a Boolean
    '''
    return Credential.credential_exist(name)

def generate_password():
    """
    function that generates unique random password
    """
    return Credential.gen_rand_pass()


def main():
    admin = User("admin","123")
    save_user(admin)
    user1 = User("clinton","pass")
    save_user(user1)
    credential1 = Credential("tiktok","joe billy","Pass231","john.doe@ymail","clinton")
    save_credential(credential1)
    credential2 = Credential("twitter","Billy joe","pass123","john.doe@ymail","clinton")
    save_credential(credential2)
    credential3 = Credential("twich","Andrew same","pass","andrew.same@ymail","admin")
    save_credential(credential3)
    credential4 = Credential("facebook","Andrew same","complex pass","same.andrew@ymail","admin")
    save_credential(credential4)
    login = False
    loggedin_user =""

    while True:
        print("Hello Welcome to your password Locker. Create an account -ca or login to account - la?")
        user_res = input().lower()

        if user_res == 'ca':
                print("New User account")
                print("-"*10)

                print ("username ....")
                username = input()

                print("password...")
                password = input()

                save_user(create_user(username,password))
                print ('\n')
                print(f"New user {username} was created, please login!!")
                print ('\n')

        elif user_res == 'la':
            print("Please enter your passLocker username and password")
            print("Username: ")
            user_name = input().lower()
            print("password: ")
            user_pass = input().lower()

            """ check if user exist otherwise return to menu """
            if(check_existing_user(user_name)):
                for user in User.user_list:
                    if user.username == user_name and user.password == user_pass:
                        login = True
                        loggedin_user = user_name
                        break

                break
            else:
                print("user login failed try agian!!!")
        else:
            print("Please use the short codes")


    while login:
        print("-"*30)
        print("Use these short codes : cd - create a new credential, dc - display credentials, fc -find a credentials, de- delete credential,ex -exit the application ")

        short_code = input().lower()

        if short_code == 'cd':
            print("New User credential")
            print("-"*10)

            print("name of credential...")
            credential_name = input()

            print ("username ....")
            username = input()

            print("manually enter a password -m or autogenerate password -a...")
            pass_ans = input()
            password = ""

            if pass_ans == "m":
                password = input()
            elif pass_ans == "a":
                password = generate_password()
                print("Random password has been generated!")
            else:
                print("Enter either m or a please")

            print("email...")
            email = input()

            save_credential(create_credential(credential_name,username,password,email,loggedin_user))
            print ('\n')
            print(f"New credential {credential_name} was created!!")
            print ('\n')
        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your credentials")
                print('\n')

                for credentials in display_credentials():
                    # i want to diplay all credentials but for a specific use
                    if credentials.creator == loggedin_user:
                        print(f"{credentials.name} {credentials.username} {credentials.password} .....{credentials.email}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the name of credential you want to search for")

            search_name = input()
            if check_existing_credential(search_name):
                    search_credential = find_credential(search_name)
                    print(f"Credential name {search_credential.name}")
                    print('-' * 20)

                    print(f"Username .......{search_credential.username}")
                    print(f"password .......{search_credential.password}")
                    print(f"Email address.......{search_credential.email}")
            else:
                    print("That credential does not exist")
        elif short_code == "de":
            print("Enter the name of credential you want to delete for")
            cred_name = input()
            if check_existing_credential(cred_name):
                res = find_credential(cred_name)
                del_credential(res)
                print(f" {res.name} was removed!")
            else:
                print("That credential does not exist")

        elif short_code == "ex":
                print("Adios .......")
                break
        else:
            print("Please use the short codes")




if __name__ == '__main__':
    main()
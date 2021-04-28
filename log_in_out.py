from user import *
#sagj
# global variables
logged_in_user = []  # the user object who is logged in
username_list = []  # list of usernames
password_list = []  # list of passwords
user_pass_dict = {}  # dictionary in which key is username and value is password
user_obj_dict = {}  # dictionary in which key is username and value is an obj of class User


def sign_up():
    """
    This function get information from user for the first time and create an account
    """
    name = input('Enter name:\n')
    family = input('Enter family:\n')
    username = input('Enter username:\n')
    for k, v in user_pass_dict.items():
        if username == k:
            username = input('Username Exists! Please Enter New Username:\n')
    phone = input('Enter phone:\n')
    # while True:
    #     phone = input('Enter phone:\n')
    #     if not isinstance(phone, int):
    #         print('Phone number should be in digit try again:')
    #     else isinstance(p)
    #         break

    email = input('Enter email:\n')
    bio = input('Enter bio:\n')
    while True:
        password1 = input('Enter password:\n')
        password2 = input('Enter password again:\n')
        if password1 != password2:
            print('password not matched')
        else:
            password = password1.__hash__()
            break

    user_pass_dict[username] = password
    username_list.append(User(username, phone, email, bio, None, name, family))
    return f'{username} \n***Congratulation you have successfully signed up! '


def sign_up_in():
    """
    This function does sign in or sign up
    """
    selection = input('Enter "u" for Sign up or "i" for Sign in:')
    if selection == 'u':
        print(sign_up())
    if selection == 'i':
        while True:
            input_username = input('Enter username:\n')
            input_password = input('Enter password:\n')
            if input_username not in username_list or user_pass_dict[input_username] != input_password:
                print('username or password wrong plz try again')
            else:
                print('***You are logged in.\n')
                logged_in_user.append(user_obj_dict[input_username])
                break

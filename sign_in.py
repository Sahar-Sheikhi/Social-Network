import hashlib

import sign_up

import user


def sign_in():
    """
    This function does sign in or sign up
    """
    while True:
        input_username = input('Enter username:\n')
        input_password = input('Enter password:\n')
        hash_input_password = hashlib.sha256(input_password.encode('utf8')).hexdigest()

        if input_username not in sign_up.usernames_list or \
                sign_up.df_saved_auth_info.loc[input_username]['Passwords'] != hash_input_password:
            print('username or password wrong plz try again')
        # elif input_username == 'r' or input_password == 'r':
        #     return 'Returning to Previous Menu'
        else:
            print(f'************ Dear {input_username} ************\n***You Have logged in Successfully!***\n')
            break
    return user.User(input_username, input_password)

# print(sign_in())
# print(sign_up.usernames_list)

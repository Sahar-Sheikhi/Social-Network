import hashlib

import user

import pandas as pd

df_saved_auth_info = pd.read_csv('authentication_info.csv', index_col=['Users'])
usernames_list = list(df_saved_auth_info.index)
# print(df_saved_auth_info.loc['sahar']['Passwords'])


# print(usernames_list)


def sign_up():
    """
    This function get information from user for the first time and create an account
    """
    while True:
        input_username = input('Enter username:\n')
        if input_username in usernames_list:
            print('Username Already Exists! Please Try Again:\n')
        else:
            break
    while True:
        password1 = input('Enter password:\n')
        password2 = input('Enter password again:\n')
        if password1 != password2:
            print('passwords are not matched! Please Try Again:\n')
        else:
            input_password = password1
            hash_password = hashlib.sha256(input_password.encode('utf8')).hexdigest()

            new_user = user.User(input_username, hash_password)
            # new_user = user.User('woody', '123', 9126129808, 'sahar@gmail.com', 'I am devops.', 'sahar', 'sheikhi')

            df_new_user_info = pd.DataFrame([[input_username, hash_password]], columns=['Users', 'Passwords'])

            df_new_user_info.to_csv('authentication_info.csv', mode='a', index=False, header=False)

            break

    return f'Dear {input_username}: \n*****************************************************\n***Congratulation' \
           f' you have successfully signed up!***\n***************************************************** '

# print(sign_up())

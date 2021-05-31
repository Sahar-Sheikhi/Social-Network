import hashlib

import pandas as pd

import logging

logging.basicConfig(filename='log_info.log', filemode='a', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(message)s')


df_saved_auth_info = pd.read_csv('authentication_info.csv', index_col=['Users'])
usernames_list = list(df_saved_auth_info.index)



def sign_up():
    """
    This function get information from user for the first time and create an account
    """
    while True:
        input_username = input('Choose a new username:\n')
        if input_username in usernames_list:
            print('Username Already Exists! Please Try Again:\n')
        else:
            print('This username is valid.')
            break
    while True:
        password1 = input('Enter password:\n')
        password2 = input('Enter password again:\n')
        if password1 != password2:
            print('passwords are not matched! Please Try Again:\n')
        else:
            input_password = password1
            hash_password = hashlib.sha256(input_password.encode('utf8')).hexdigest()
            df_new_user_info = pd.DataFrame([[input_username, hash_password]], columns=['Users', 'Passwords'])
            df_new_user_info.to_csv('authentication_info.csv', mode='a', index=False, header=False)
            logging.info('Successful Register')
            break

    return f'Dear {input_username}: \n*****************************************************\n***Congratulation' \
           f' you have successfully signed up!***\n***************************************************** '


import hashlib
import logging

import pandas as pd

import sign_up

import user

import time


def sign_in():
    """
    This function does sign in or sign up
    """
    df_saved_auth_info = pd.read_csv('authentication_info.csv', index_col=['Users'])
    usernames_list = list(df_saved_auth_info.index)
    while True:
        input_counter = 3
        while True:
            input_username = input('Enter username:\n')
            input_password = input('Enter password:\n')
            hash_input_password = hashlib.sha256(input_password.encode('utf8')).hexdigest()

            if input_username not in usernames_list or \
                    df_saved_auth_info.loc[input_username]['Passwords'] != hash_input_password:
                print('username or password wrong plz try again')
                logging.info('Unsuccessful Login')
                input_counter -= 1
                # check if user had 3 wrong tries then wait for 10 seconds
                if input_counter == 0:
                    print('You Entered Wrong info 3 times! Please wait for 10 seconds then try again.')
                    logging.warning('invalid data entered 3 times')
                    time.sleep(10)
                    break

            else:
                print(f'************ Dear {input_username} ************\n***You Have logged in Successfully!***\n')
                logging.info('Successful Login')
                return user.User(input_username, input_password)


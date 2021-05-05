import hashlib

import user

import csv

import re

import pandas as pd

file_path = 'info.csv'
df_saved_info = pd.read_csv(file_path)
username_list = (list(df_saved_info.iloc[:, 0]))


def sign_up():
    """
    This function get information from user for the first time and create an account
    """

    input_name = input('Enter name:\n')
    input_family = input('Enter family:\n')

    phone_frmt = '^09[\d]{9}$'
    while True:
        input_phone = input('Enter Your Phone Number:\n')
        if not re.search(phone_frmt, input_phone):
            print('Phone Number Format is not valid')
        else:
            break

    email_frmt = '^[\w]+@[\w]+\.\w+$'
    while True:
        input_email = input('Enter email:\n')
        if not re.search(email_frmt, input_email):
            print('Email Format is not valid')
        else:
            break

    input_bio = input('Enter bio:\n')

    while True:
        input_username = input('Enter username:\n')
        if input_username in username_list:
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

            new_user = user.User(input_username, hash_password, input_phone, input_email,
                                 input_bio, input_name, input_family)
            # new_user = user.User('woody', '123', 9126129808, 'sahar@gmail.com', 'I am devops.', 'sahar', 'sheikhi')

            df_new_user_info = pd.DataFrame([[input_username, hash_password]],columns= ['Users', 'Passwords'])

            df_new_user_info.to_csv(file_path,mode='a', index=False)

            break

    return f'Dear {input_name}: \n*****************************************************\n***Congratulation' \
           f' you have successfully signed up!***\n***************************************************** '



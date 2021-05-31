import re

import pandas as pd

# df_saved_prof_info = pd.read_csv('profile_info.csv', index_col=['Username'])



class Profile:
    def __init__(self, username, password = None, name=None, family=None, phone=None, email=None, bio=None):
        self.username = username
        self.name = name
        self.family = family
        self.phone = phone
        self.email = email
        self.bio = bio
        self.password = password


    def set_phone(self,input_phone):
        """
        Check phone format
        """
        phone_frmt = '^09[\d]{9}$'
        if not re.search(phone_frmt, input_phone):
            print('Phone Number Format is not valid')
            return False
        self.phone = input_phone

    def set_email(self, input_email):
        """
        Check email format
        """
        email_frmt = '^[\w]+@[\w]+\.\w+$'
        if not re.search(email_frmt, input_email):
            print('Email Format is not valid')
            return False
        self.email = input_email



    def edit_profile(self, name, family, phone, email, bio):
        self.name = name
        self.family = family
        self.set_phone(phone)
        self.phone = phone
        self.set_email(email)
        self.bio = bio



    def change_password(self,new_password):
        self.password = new_password



    def __str__(self):
        return f'{self.username} {self.phone} {self.email} {self.bio} {self.name} {self.family}'



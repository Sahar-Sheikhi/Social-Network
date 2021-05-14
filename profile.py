import re

import pandas as pd

df_saved_prof_info = pd.read_csv('profile_info.csv', index_col=['Username'])


# print(dict(df_saved_prof_info.loc['woody']))

class Profile:
    def __init__(self, username, name=None, family=None, phone=None, email=None, bio=None):
        self.username = username
        self.name = name
        self.family = family
        self.phone = phone
        self.email = email
        self.bio = bio

    def edit_profile(self, name, family, phone, email, bio):
        self.name = name
        self.family = family
        self.set_phone(phone)
        self.phone = phone
        self.set_email(email)
        self.bio = bio

    def set_phone(self,phone):
         phone_frmt = '^09[\d]{9}$'
         if not re.search(phone_frmt, input_phone):
             print('Phone Number Format is not valid')
         else:
                self.phone = phone

    def set_email(self, email):

        email_frmt = '^[\w]+@[\w]+\.\w+$'
        if not re.search(email_frmt, email):
            print('Email Format is not valid')
        else:
            self.email = email

    # @classmethod
    # def get_profile_info(cls, user):
    #     """
    #     Get data from user and check validity and return a list of profile attributes
    #     """
    #     input_name = input('Enter Name:\n')
    #     input_family = input('Enter family:\n')
    #     phone_frmt = '^09[\d]{9}$'
    #     while True:
    #         input_phone = input('Enter Your Phone Number:\n')
    #         if not re.search(phone_frmt, input_phone):
    #             print('Phone Number Format is not valid')
    #         else:
    #             input_phone = input_phone
    #             break
    #
    #     input_bio = input('Enter bio:\n')
    #     profile = cls(input_name, input_family, input_phone, input_email, input_bio)
    #     return profile

    def __str__(self):
        return f'{self.username} {self.phone} {self.email} {self.bio} {self.name} {self.family}'

# profile1= Profile('sahar')
# print(profile1.edit_profile())

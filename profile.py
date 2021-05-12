
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

    def edit_profile(self,name,family,phone,email,bio):
        self.name = name
        self.family = family
        self.phone = phone
        self.email = email
        self.bio = bio


    def __str__(self):
        return f'{self.username} {self.phone} {self.email} {self.bio} {self.name} {self.family}'

# profile1= Profile('sahar')
# print(profile1.edit_profile())
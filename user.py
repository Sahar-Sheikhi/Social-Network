import profile

import post
from Social_Network import comment


class User:
    def __init__(self, username, password, profile=None):
        self.username = username
        self.password = password
        self.profile = profile
        self.friends = []
        self.posts = []


    def set_profile(self):
        """
        This Function Set profile for user in first log in
        """
        self.profile = profile.Profile(self.username)



    def set_friends(self, friend_username):
        """
        This Function set friends list
        """
        self.friends.append(friend_username)
        return f'{friend_username} is Your Friend Now!'

    def __str__(self):
        return f'{self.username}'


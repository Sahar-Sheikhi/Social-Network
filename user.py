import profile

import post
from Social_Network import comment


class User:
    def __init__(self, username, password, profile=None, post_num=0):
        self.username = username
        self.password = password
        self.profile = profile
        self.friends = ['test friend','woody']
        self.posts = []
        self.post_num = post_num

    def set_profile(self):
        # user_profile = profile.Profile(self.username)
        self.profile = profile.Profile(self.username)


    def set_friends(self,friend_username):
        """
        This Function set friends list
        """
        self.friends.append(friend_username)
        return f'{friend_username} is Your Friend Now!'



    def __str__(self):
        return f'{self.username}'


user1 = User('woody', '123')
# print(user1)
# print(user1.new_post())
# user1.set_profile()
# # print(user1.profile)
# user1.send_post()
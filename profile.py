

from Social_Network.user import User


class Profile(User):
    def __init__(self, username):
        self.username = username



    def edit_profile(self):
        self.name= input('Enter Name:\n')

    def __str__(self):

        return f''

# profile1= Profile()
# print(profile1.name)

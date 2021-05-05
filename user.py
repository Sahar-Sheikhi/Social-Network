import profile

import post


class User:
    def __init__(self, username, password, phone, email, bio, name=None, family=None):
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.bio = bio
        self.friends = []
        self.posts = []
        # self.profile = profile.Profile(username, password, phone, email, bio, name, family)

    def show_profile(self):
        """
        This Function show profile
        """
        return f'profile:{self.name} {self.family} {self.bio}'

    def new_post(self):
        """
        This Function create a new post for the user
        """
        user_new_post = post.Post()
        self.posts.append(user_new_post)
        return user_new_post.new_post()

    def set_comment(self, post, editor):
        editor = self.username

    #
    # def set_friends(self):
    #     """
    #     This Function set friends list
    #     """

    def __str__(self):
        return f'{self.username} {self.phone} {self.email} {self.bio}{self.name} {self.family}'


user1 = User('woody', '123', 9126129808, 'sahar@gmail.com', 'I am devops.', 'sahar', 'sheikhi')
# print(user1.new_post())

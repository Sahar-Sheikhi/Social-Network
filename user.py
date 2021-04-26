from post import *
class User:
    def __init__(self, username, password, phone, email, bio, posts=[], friends=[], name=None, family=None):
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.bio = bio
        self.friends = friends
        self.posts = posts

    def show_profile(self):
        """
        This Function show profile
        """
        return f'profile:{self.name} {self.family} {self.bio}'

    def edit_post(self, post_content):
        """
        This Function create a post for a user
        """
        print('This Function create a post for a user')
        # post_content = input('enter txt')
        # new_post = Post(post_content)
        # new_post.get_post()
        # self.posts.append()

    def set_friends(self):
        """
        This Function set friends list
        """
        return ('This Function set friends list')


    def __str__(self):
        return f'{self.phone} {self.email} {self.bio}{self.profile}'


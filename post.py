import comment

import datetime

import pytz


class Post:
    def __init__(self, post_content=None, timestamp=0, comment_num=0):
        """
        post_content= post post_content
        date= date of modification
        timestamp=timestamp of modification
        comment=comment about a post by other users
        comment-num=number of comments for a post
        """
        self.comment = []
        self.post_content = post_content
        self.timestamp = timestamp
        self.comment_num = comment_num

    # def show_post(self):

    def new_post(self):
        input_content = input('Write Post Content:\n')
        self.post_content = input_content
        time_zone = pytz.timezone('Asia/Tehran')
        self.timestamp = datetime.datetime.now(time_zone).strftime("%Y-%m-%d   %H:%M:%S")

        return f'New Post is Created Successfuly at:{self.timestamp}'

    # def edit_post(self):
    #    """
    #     This Function create, modify or delete post
    #     """
    #
    #     self.post_content =input('Write Post:\n')
    #     return Post(self.text, datetime.datetime.now(), datetime.datetime.today())

    def set_comment(self,editor):
        """
        This Function create comment for a post and set comment_num
        """
        post_comment = comment.Comment(editor)
        self.comment_num += 1

    def __str__(self):
        return f'{self.date} {self.date} {self.time} {self.comment} {self.comment_num}'

#
# post1 = Post()
# print(post1.new_post())

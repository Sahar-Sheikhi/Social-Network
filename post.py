import pandas as pd

import comment

df_saved_post_info = pd.read_csv('post_info.csv', index_col=['Post_ID'])


# print(list(df_saved_post_info.loc['sahar_1']))

class Post:
    def __init__(self, username, comment_editor=None, post_content=None, comment_num=0, post_id=None):
        """
        post_content= post post_content
        date= date of modification
        timestamp=timestamp of modification
        comment=comment about a post by other users
        comment-num=number of comments for a post
        """
        self.username = username
        self.post_id = post_id
        self.comment_editor = comment_editor
        self.comment = []
        self.post_content = post_content
        # self.timestamp = timestamp
        self.comment_num = comment_num

    # Send New Post
    def new_post(self, user_post_index, timestamp):
        """
               This Function send a new post for the user
        """
        # set post_id from username and number of post
        self.post_id = self.username + '_' + str(user_post_index + 1)

        return f'New Post is Sent Successfuly at:{timestamp}'

    def edit_post(self, new_content, timestamp):
        self.post_content = new_content
        print(f'Your Post Edited Successfully at {timestamp}')
        return [self.post_content, timestamp]

    def set_comment(self):
        """
               This Function set a comment for the post
        """
        # pass username as editor and post_id to create a new comment object

        post_comment = comment.Comment(self.username)
        self.comment_num += 1

        return post_comment.new_comment(self.comment_num)

    # def edit_post(self,input_content):
    #    """
    #     This Function create, modify or delete post
    #     """
    #
    #     self.post_content =input_content
    #     return Post(self.text, datetime.datetime.now(), datetime.datetime.today())

    def __str__(self):
        return f'Post Content: {self.post_content}  has {self.comment_num} Comments'

#
# post1 = Post('sahar')
# print(post1.new_post(1))

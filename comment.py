import datetime

import pandas as pd

import pytz


class Comment:
    def __init__(self, comment_editor, post_comment_index=1, post_id=None, comment_content=None, comment_id=None):
        self.post_comment_index = post_comment_index
        self.comment_content = comment_content
        self.post_id = post_id
        self.comment_editor = comment_editor
        self.comment_id = comment_id

    def new_comment(self, new_content, post_cmnt_index ,timestamp):
        """
        This Function send a new comment
        """
        self.comment_id = self.post_id + '_' + str(self.post_comment_index)
        self.comment_content = new_content
        self.post_comment_index = str(post_cmnt_index)

        return f'Your Comment is Sent Successfully at {timestamp}'

    # @staticmethod
    # def set_comment(editor):
    #     """
    #     This Function create comment for a post and set comment_num
    #     """
    #     post_comment = comment.Comment(editor)
    #     self.comment_num += 1

#
# comment1 = Comment('sahar', 'sahar-1')
# print(comment1.new_comment())

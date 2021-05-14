import datetime

import pandas as pd

import pytz


class Comment:
    def __init__(self, comment_editor, post_id=None, comment_content=None, timestamp=None, comment_id=None):
        self.timestamp = timestamp
        self.comment_content = comment_content
        self.post_id = post_id
        self.comment_editor = comment_editor
        self.comment_id = comment_id

    def new_comment(self, post_comment_index):
        """
        This Function send a new comment
        """
        self.comment_content = input('Write Comment:\n')
        time_zone = pytz.timezone('Asia/Tehran')
        self.timestamp = datetime.datetime.now(time_zone).strftime("%Y-%m-%d   %H:%M:%S")
        self.comment_id = self.post_id + '/' + str(self.comment_editor) + '/' + str(post_comment_index)
        df_new_comment = pd.DataFrame([[self.comment_id, self.post_id, self.comment_editor,
                                        self.comment_content, self.timestamp]]
                                      , columns=['Comment_ID', 'Post_ID', 'Editor', 'Content', 'Timestamp'])
        df_new_comment.to_csv('comment_info.csv', mode='a', index=False, header=False)

        return f'Your Comment is Sent Successfully at {self.timestamp}'

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

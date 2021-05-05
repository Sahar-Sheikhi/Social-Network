import datetime


class Comment:
    def __init__(self,comment_content, timestamp, editor):
        self.comment_content = comment_content
        self.timestamp = timestamp
        self.editor = editor

    def set_comment(self, editor):
        input_content = input('Write Comment:\n')
        self.comment_content = input_content
        time_zone = pytz.timezone('Asia/Tehran')
        self.timestamp = datetime.datetime.now(time_zone).strftime("%Y-%m-%d   %H:%M:%S")
        self.editor = editor
        return f' Successfully at {self.timestamp}'



# comment1 = Comment()

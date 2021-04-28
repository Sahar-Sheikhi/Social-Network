import datetime
#da

class Post:
    def __init__(self, text, date=0, time=0, comment=None, comment_num=0):
        """
        text= post content
        date= date of modification
        time=time of modification
        comment=comment about a post by other users
        comment-num=number of comments for a post
        """
        self.comment = comment
        self.text = text
        self.date = date
        self.time = time
        self.comment_num = comment_num

    def show_post(self):
        print('show content of a post')

    def edit_post(self):
        """
        This Function create, modify or delete post
        """
        self.text = input('Write Post:\n')
        return Post(self.text, datetime.datetime.now(), datetime.datetime.today())

    def set_comment(self):
        """
        This Function create comment for a post and set comment_num
        """
        # self.comment = input('Write comment:\n')
        # self.comment_num += 1
        print('set comment')

    def __str__(self):
        return f'{self.date} {self.date} {self.time} {self.comment} {self.comment_num}'

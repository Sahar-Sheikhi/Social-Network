import datetime
import hashlib

import importlib

import logging

import pytz

from Social_Network.comment import Comment
from Social_Network.csv_functions import read_file_row, read_file_index, save_data, read_file_cell, edit_data
from Social_Network.json_functions import read_json_file, write_json_file, edit_json
from Social_Network.post import Post
from Social_Network.sign_up import usernames_list

# CSV files path
auth_file_path = 'authentication_info.csv'
profile_path = 'profile_info.csv'
post_file_path = 'post_info.csv'
comment_file_path = 'comment_info.csv'

# Json file path
friends_file_path = 'friends_info.json'


# csv files headers
auth_file_headers= ['Users', 'Passwords']
profile_file_headers= ['Name', 'Family', 'Phone', 'Email', 'Bio']
post_file_headers_list= ['Post_ID', 'Content', 'Timestamp', 'NumOfComment']
comment_file_headers_list= ['Comment_ID', 'Post_ID', 'Editor', 'Content', 'Timestamp']



def set_timestamp():
    """
     Set date and time as timestamp
    """
    time_zone = pytz.timezone('Asia/Tehran')
    timestamp = datetime.datetime.now(time_zone).strftime("%Y-%m-%d[%H:%M:%S]")
    return timestamp


def print_list_index(given_list, msg):
    """
    get a list and print its elements with index

    """
    if type(given_list) == bool:
        print(msg)
        return False
    else:
        if len(given_list) != 0:
            for element in range(len(given_list)):
                print(f'{element + 1}) {given_list[element]}')
        elif len(given_list) == 0:
            print(msg)
            return False

        else:
            print('not list')


def yes_no_menu(method, action_name, *args):
    """
     Menu to ask user to do a mthod or not
     return method or False due to user decision
    """
    while True:
        try:
            entered_key = input(f'\n***Do You Want to {action_name}?(Y/N)\n').lower()
            assert entered_key in ['y', 'n']
            if entered_key == 'y':
                if method is None:
                    return ''
                else:
                    return method(*args)
            elif entered_key == 'n':
                return False

        except AssertionError:
            print('Invalid Input!Try Again Please')


def exist_in_index(given_list, value):
    """
    This Function check if value exists in list elements
    return list of elements which consist value
    """
    value_ls = []  # list of elements which consist value in their string
    for element in given_list:
        if element.startswith(value):
            value_ls.append(element)
    if len(value_ls) != 0:
        return value_ls
    else:
        return False


def check_input_validity(msg):
    """
    This Function get an input from user check whether it is integer or not
    msg: represents a string which appears for the user
    return user input
    """
    while True:
        try:
            entered_input = int(input(msg))
            if entered_input == 0:
                print('~~~Going to previous Menu...')
                return 0
            else:
                return entered_input
        except ValueError:
            print('Wrong Input! Please Try Again\n')


# all_post_cmnt_ls = read_file_index(comment_file_path, 'Post_ID')


# Fuctions in main file used to to an action for signed_in user


def show_prof(signed_user):
    """
    This Function Show Profile of user
    user : represents a user class object
    return list of profile attributes of the user
    """
    user_profile_list = read_file_row("profile_info.csv", "Username", signed_user.username,
                                      'Your Profile is Empty Yet!')
    print(f'~~~~~~~~~~~  Your Profile  ~~~~~~~~~~~\n{user_profile_list}')
    return user_profile_list


def edit_prof(user):
    user_choice = yes_no_menu(None, 'Edit Profile', )
    if user_choice is False:
        return 'Going to previous Menu'
    else:
        input_name = input('Enter Name:\n')
        input_family = input('Enter family:\n')
        while True:
            input_phone = input('Enter phone(Press "s" to skip):\n')
            if input_phone == 's':
                input_phone = ''
                break
            elif user.profile.set_phone(input_phone) is not False:
                break

        while True:
            input_email = input('Enter email(Press "s" to skip):\n')
            if input_email == 's':
                input_email = ''
                break
            elif user.profile.set_email(input_email) is not False or input_email == 's':
                break

        try:
            input_bio = input('Enter bio:\n')
        except KeyboardInterrupt:
            input_bio = ''
        user.profile.edit_profile(input_name, input_family, input_phone, input_email, input_bio)
        logging.info(f'Username:[{user.username}] Edited Profile')
        edit_data(profile_path, 'Username', user.username, ['Name', 'Family', 'Phone', 'Email', 'Bio'],
                  [input_name, input_family, input_phone, input_email, input_bio])

def change_pass(user):

    yes_no_menu(user.profile.change_password,'Change Password', 1)

    while True:
        new_pass1 = input('Enter new password:\n')
        new_pass2 = input('Enter new password again:\n')
        if new_pass1 != new_pass2:
            print('passwords are not matched! Please Try Again:\n')
        else:
            new_pass = new_pass1
            user.profile.change_password(new_pass)
            print('Your password changed successfully!')
            logging.info(f'{user.username} changed password')
            hash_new_pass = hashlib.sha256(new_pass.encode('utf8')).hexdigest()
            edit_data(auth_file_path, 'Users', user.username, ['Passwords'], [hash_new_pass])
            break


def send_post(user):
    all_postid_ls = read_file_index(post_file_path, 'Post_ID')
    user_post_ls = exist_in_index(all_postid_ls, user.username)  # show the num of posts of user
    if user_post_ls is False:
        user_post_no = 1  # this is the user first post
    else:
        user_post_no = len(user_post_ls) + 1

    # create a post obj for user

    new_user_post = Post(user.username, user_post_no)
    input_content = input('Write Post Content:\n')
    new_post_timestamp = set_timestamp()
    print(new_user_post.new_post(input_content, new_post_timestamp))
    logging.info(f'Username:[{user.username}] Sent a post')
    save_data(post_file_path, [new_user_post.post_id, new_user_post.post_content,
                               new_post_timestamp, new_user_post.comment_num], post_file_headers_list)


def unfollow(username, new_username_list):
    edit_json(friends_file_path, username, new_username_list)
    return 'The selected friend unfollowed!'


def see_friend_profile(user):
    print('_______________\n***Your Friends List***:')
    # show all friends listed with index to choose from
    sign_in_user_friends_ls = read_json_file(friends_file_path, user.username)
    friends_list_status = print_list_index(sign_in_user_friends_ls, 'You Have No Follower Yet!')

    # select a friend and see the profile
    if friends_list_status is False:  # user has no friend
        return ''
    else:  # user has friend
        while True:
            entered_key3 = int(input('\n\n***Choose a Friend to see the profile '
                                     '(Press "0" to Return):***\n\n'))
            friend_username = sign_in_user_friends_ls[entered_key3 - 1]
            if entered_key3 == 0:
                print('Returning to Previous Menu...')
            elif entered_key3 in range(1, len(sign_in_user_friends_ls) + 1):
                print(f'~~~{friend_username} Profile~~~')
                print(read_file_row(profile_path, 'Username', friend_username, ''))
                # unfollow a friend
                # print('Do You want to unfollow this friend?\n')
                sign_in_user_friends_ls.remove(friend_username)
                print(yes_no_menu(unfollow, 'Unfollow this friend?', user.username, sign_in_user_friends_ls))
                # unfollow(user.username, sign_in_user_friends_ls)
                break
            else:
                print('Wrong Input! Please Try Again.')


def show_edit_post(user):
    """
    This Function show and edit posts of a user
    uesr: represents an obj of User class

    """
    # Show Posts
    postid_ls = read_file_index(post_file_path, 'Post_ID')  # list of all post_ID
    user_postid_ls = exist_in_index(postid_ls, user.username)  # list post_ID for user

    # Check whether user has any post to show or not
    if len(user_postid_ls) == 0:
        print('~~~You Have No Post Yet!~~~\n')
        yes_no_menu(send_post, 'Send a Post', user)
    else:
        for _ in range(len(user_postid_ls)):
            print(f'{_ + 1}){read_file_row("post_info.csv", "Post_ID", user_postid_ls[_], "")}')

        # Edit Posts
        while True:
            try:
                input_post_index = int(input('Select a Post to edit (Enter the number):\n'))
                user_post_count = len(user_postid_ls)
                assert input_post_index in range(user_post_count + 1)
                if input_post_index in range(1, user_post_count + 1):
                    selected_post = user_postid_ls[input_post_index - 1]
                    new_post_content = check_input_validity('Write New Content(Enter "0" to Return):\n')
                    if new_post_content == 0:
                        break
                    else:
                        new_post_timestamp = set_timestamp()

                        # Update post file with new data
                        edit_data(post_file_path, 'Post_ID', selected_post,
                                  ['Content', 'Timestamp'], [new_post_content, new_post_timestamp])
                elif input_post_index == 0:
                    print('~~~~Going to previous menu...')
                    break
            except AssertionError:
                print('Your input is not valid!Try Again Please ')

            except ValueError:
                print('Enter a Number!Try Again Please ')


def users_post_comment_show_edit(user):
    # ****** sign_in selects a user from all users list
    while True:
        # Print all Users list
        print_list_index(usernames_list, 'No users yet!')
        # Select user menu
        entered_key5 = int(input('***Choose a User(Press "0" to Return):***\n_______________\n\nUsers List:'))
        if entered_key5 not in range(len(usernames_list) + 1):
            print('Wrong Input! Please Try Again.')
        elif entered_key5 == '0':
            print('Returning to Previous Menu...')
            break

        # ****** show posts of selected user
        else:
            selected_user_username = (usernames_list[entered_key5 - 1])
            # all_postid_ls represents all post_IDs
            all_postid_ls = read_file_index(post_file_path, 'Post_ID')

            # selected_user_postid: represents list of posts of selected user
            selected_user_postid_ls = exist_in_index(all_postid_ls, selected_user_username)

            # ****** show posts of selected user
            print(f'~~~{selected_user_username} Posts:')
            if selected_user_postid_ls is False:
                print('User has no Post')
                break
            else:
                for post_id in selected_user_postid_ls:
                    print(read_file_row(post_file_path, 'Post_ID', post_id, ' Has No Post'))
                # selected_user_postid_row = list(read_file_row(post_file_path, 'Post_ID', post_id, ' Has No Post'))

                # menu to choose post
                entered_key5_1 = check_input_validity('***Enter a Post Number To See its Comments (Press "0" to Return):***'
                                                      '\nselected post_number is:')
                if entered_key5_1 == 0:  # when selected user has no post
                    print('Going to Previous Menu...')
                    break
                else:  # when selected user has post

                    # ****** Show Comment for Selected Post
                    # Create Comment_ID from selected post_ID and entered index by sign_in user
                    selected_post_cmnt_id = selected_user_postid_ls[entered_key5_1 - 1] + '_' + str(entered_key5_1)
                    selected_user_postid = selected_user_postid_ls[entered_key5_1 - 1]
                    # show all comments of selected post
                    # read comment of selected post id (pandas dataframe type)
                    print(read_file_row(comment_file_path, 'Comment_ID',
                                        selected_post_cmnt_id, 'This Post has no comment'))
                    # get the commnet number of a post
                    post_numofcmnt = int(read_file_cell(post_file_path, 'Post_ID', selected_user_postid,
                                                    'NumOfComment', 'No such post'))
                    if post_numofcmnt == 0:  # first comment
                        post_numofcmnt = 1
                    else:
                        post_numofcmnt += 1
                    post_numofcmnt = str(post_numofcmnt)
                    # Send New Comment
                    # create a comment obj for post
                    new_post_cmnt = Comment(user.username, post_numofcmnt, selected_user_postid)
                    # ask user whether to send a comment or not
                    input_content = yes_no_menu(input, 'Send Comment Content:\n', 'Write your comment text: ')
                    new_comment_timestamp = set_timestamp()
                    print(new_post_cmnt.new_comment(input_content, post_numofcmnt, new_comment_timestamp))
                    logging.info(f'Username:[{user.username}] send a comment')
                    # edit_data(post_file_path, 'Post_ID', selected_user_postid, ['Content', 'Timestamp', 'NumOfComment'],selected_user_postid_row)
                    save_data(comment_file_path, [new_post_cmnt.comment_id, new_post_cmnt.post_id,
                                                  new_post_cmnt.comment_editor, new_post_cmnt.comment_content,
                                                  new_comment_timestamp], comment_file_headers_list)
                    break

        break


def follow(user):
    print_list_index(usernames_list, 'No Users Found Yet')  # print users with index to let the sign_in user choose from
    # show profile for selected user
    while True:
        entered_key4_1 = int(input('\n\n***Choose a User to See Profile (Enter a Number): '
                                   '(Press "0" to Return):***\n\n'))
        if entered_key4_1 in range(1, len(usernames_list) + 1):
            selected_user_username = (usernames_list[entered_key4_1 - 1])  # username of the user who is selected
            print(f'~~~{selected_user_username} Profile~~~')
            print(read_file_row('profile_info.csv', 'Username', selected_user_username, ''))

            # Follow a user as friend
            print(yes_no_menu(user.set_friends, 'Add a Friend', selected_user_username))
            write_json_file(friends_file_path, user.username, selected_user_username)

        elif entered_key4_1 == 0:
            print('Returning to Previous Menu...')
            break
        else:
            print('Wrong Input! Please Try Again.')

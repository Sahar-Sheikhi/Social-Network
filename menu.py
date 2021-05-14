import datetime

import pytz

import json

import os

import pandas as pd

from Social_Network import post
from Social_Network.sign_up import usernames_list

# CSV files path
auth_file_path = 'authentication_info.csv'
profile_path = 'profile_info.csv'
post_file_path = 'post_info.csv'
comment_file_path = 'comment_info.csv'
friends_file_path = 'friends_info.json'


def set_timestamp():
    """
     Set date and time as timestamp
    """
    time_zone = pytz.timezone('Asia/Tehran')
    timestamp = datetime.datetime.now(time_zone).strftime("%Y-%m-%d[%H:%M:%S]")
    return timestamp


def print_list_index(list):
    """
    get a list and print its elements with index
    """
    for _ in range(len(list)):
        print(f'{_ + 1}) {list[_]}')


def yes_no_menu(method, action_name, *args):
    """
     Menu to ask user to do a mthod or not
    """
    while True:
        try:
            entered_key = input(f'\n***Do You Want to {action_name}?(Y/N)\n').lower()
            assert entered_key in ['y', 'n']
            if entered_key == 'y':
                if len(args) == 0:
                    return method()
                else:
                    return method(args)
                break

            elif entered_key == 'n':
                return None
                break

        except AssertionError:
            print('Invalid Input!Try Again Please')



def save_data(path, attr_ls, header_ls):
    """
    Save data to a csv file
    path:file path
    attr_list=input data
    header_ls=headers list for input data
    """
    df_save = pd.DataFrame([attr_ls], columns=header_ls)
    df_save.to_csv(path, mode='a', index=False, header=False)


def read_data(path, index_name, value):
    """
    Save data to a csv file
    path:file path
    index: represents dataframe index name(str)
    """

    df_read = pd.read_csv(path, index_col=index_name)
    if value in df_read.index:
        return df_read.loc[value]
    else:
        return f'No related data found !'


def read_file_index(path, index_name):
    """
    Save data to a csv file
    path:file path
    index: represents dataframe index name(str)
    return a list of index
    """
    df_read = pd.read_csv(path, index_col=index_name)
    return list(df_read.index)


def edit_data(path, index_name, index_value, header_name_ls, new_value_ls):
    """
    This Function updates only a row in csv based on given index_name
    header_name_ls: represents list of headers
    new_value_ls: represents list of new values
    """
    df_read = pd.read_csv(path, index_col=index_name)
    for _ in range(len(header_name_ls)):
        df_read.loc[index_value, header_name_ls[_]] = new_value_ls[_]
    df_read.to_csv(path, mode='w', index=True, header=True)


def exist_in_index(list, value):
    for _ in list:
        if _.startswith(value):
            return True
        else:
            continue


def read_json_file(path, key):
    """
    This Function get a json file path and a key and return the value as a list
    path: represent a json file path
    key: represent a key in dict saved in json file
    """
    with open(path) as handler:
        read_dict = json.load(handler)
    return read_dict[key]


# Fuctions in main file used to to an action for signed_in user
def show_edit_profile(user):
    # Show Profile
    print(f'~~~Your Profile~~~\n{read_data("profile_info.csv", "Username", user.username)}')

    # Edit Profile
    print('~~~~~~~~~~~~~\nPlease fill your Profile')
    input_name = input('Enter Name:\n')
    input_family = input('Enter family:\n')
    input_phone = input('Enter phone:\n')
    input_email = input('Enter email:\n')
    input_bio = input('Enter bio:\n')
    user.profile.edit_profile(input_name, input_family, input_phone, input_email, input_bio)


def send_post(user):
    user_post = post.Post(user.username)
    user_post.post_content = input('Write Post Content:\n')
    user_post_timestamp = set_timestamp()
    user_post_index = len(user.posts)
    print(user_post.new_post(user_post_index, user_post_timestamp))
    save_data(post_file_path,
              [user_post.post_id, user_post.post_content, user_post_timestamp, user_post.comment_num],
              ['Post_ID', 'Content', 'Timestamp', 'NumOfComment'])


def see_friend_profile(user):
    print('_______________\n***Your Friends List:')
    # show all friends listed with index to choose from
    sign_in_user_friends_ls = read_json_file(friends_file_path, user.username)
    print_list_index(sign_in_user_friends_ls)
    while True:
        entered_key3 = int(input('\n\n***Choose a Friend to see the profile '
                                 '(Press "0" to Return):***\n\n'))
        if entered_key3 in range(1, len(sign_in_user_friends_ls) + 1):
            friend_username = (sign_in_user_friends_ls[entered_key3 - 1])
            print(f'~~~{friend_username} Profile~~~')
            print(read_data(profile_path, 'Username', friend_username))
            break
        elif entered_key3 == 0:
            print('Returning to Previous Menu...')
            break
        else:
            print('Wrong Input! Please Try Again.')


def show_edit_post(user):
    """
    This Function show and edit posts of a user
    """
    # Show Posts
    user_postid_ls = read_file_index('post_info.csv', 'Post_ID')  # list post_ID for sign_in user
    if not exist_in_index(user_postid_ls, user.username):
        print('~~~You Have No Post Yet!~~~\n')
        yes_no_menu(send_post, 'Send a Post')
    else:
        for _ in range(len(user_postid_ls)):
            print(f'{_ + 1}){read_data("post_info.csv", "Post_ID", user_postid_ls[_])}')

        # Edit Posts
        input_post_index = int(input('Select a Post to edit (Enter the number):\n'))
        selected_post = user_postid_ls[input_post_index - 1]
        new_post_content = input('Enter New Content:\n')
        new_post_timestamp = set_timestamp()
        # Update post file with new data
        edit_data(post_file_path, 'Post_ID', selected_post,
                  ['Content', 'Timestamp'], [new_post_content, new_post_timestamp])


def users_post_comment_show_edit(user):
    while True:
        print('***Choose a User(Press "0" to Return):***\n_______________\n\nUsers List:')
        print_list_index(usernames_list)
        entered_key5 = int(input())
        if entered_key5 not in range(len(usernames_list) + 1):
            print('Wrong Input! Please Try Again.')
        elif entered_key5 == '0':
            print('Returning to Previous Menu...')
            break
        else:
            selected_user = (usernames_list[entered_key5 - 1])
            usr_post_id_list = []
            selected_user_post_count = 0  # counter to count the number of selected user posts
            df_saved_post_info = pd.read_csv('post_info.csv', index_col=['ID'])
            print(f'~~~{selected_user} Posts:')
            for postid in list(df_saved_post_info.index):
                if selected_user in postid:
                    selected_user_post_count += 1  # just to show index for posts of a user
                    usr_post_id_list.append(postid)  # keep post_id in a list to send comment by post_id
                    selected_user_post = dict(
                        df_saved_post_info.loc[postid])  # show user posts through dictionary type
                    if bool(selected_user_post):  # check whether selected user has post or not
                        print(f'{selected_user_post_count}:{selected_user_post}')
                else:
                    if selected_user_post_count == 0:
                        print(f'{selected_user} has no Post!')
                        break
            if selected_user_post_count != 0:
                # yes_no_option(post.Post.set_comment, usr_post_id_list, 'Send Comment')
                while True:  # Menu For Send Comment for a Post
                    entered_key5_1 = input('\n***Do You Want to Send Comment?(Y/N)\n')
                    if entered_key5_1 in ['y', 'Y']:
                        selected_post_index = int(input('Which Post?(Enter a number)'))
                        selected_post = post.Post(usr_post_id_list[selected_post_index - 1], user)
                        print(selected_post.set_comment())
                        break
                    elif entered_key5_1 in ['n', 'N']:
                        break
                    else:
                        print('Wrong Input!Try Again Please')
                break


def follow_unfollow(user):
    print_list_index(usernames_list)  # print users with index to let the sign_in user choose from
    # show profile for selected user
    while True:
        entered_key4_1 = int(input('\n\n***Choose a User to See Profile (Enter a Number): '
                                   '(Press "0" to Return):***\n\n'))
        if entered_key4_1 in range(1, len(usernames_list) + 1):
            selected_user_username = (usernames_list[entered_key4_1 - 1])  # username of the user who is selected
            print(f'~~~{selected_user_username} Profile~~~')
            print(read_data('profile_info.csv', 'Username', selected_user_username))

            # Follow a user as friend
            print(yes_no_menu(user.set_friends, 'Add a Friend', selected_user_username))
            try:
                if not os.stat(friends_file_path).st_size > 0:
                    # Save friends list in a json file for sign_in user for the first time
                    with open(friends_file_path, "a") as handler:
                        json.dump({user.username: []}, handler)
                else:
                    sign_in_user_friends_ls = read_json_file(friends_file_path, user.username)
                    sign_in_user_friends_ls.append(selected_user_username)

                    added_friend_dict = {
                        user.username: user.friends
                    }

                    with open(friends_file_path, "a") as handler:
                        json.dump(added_friend_dict, handler)
                    break
            except OSError as oserr:
                print(oserr)

            # try:
            #     with open(friends_file_path) as handler:
            #         added_friend_dict = json.load(handler)
            # except FileNotFoundError as fnf_error:
            #     print(fnf_error)
            # except Exception as e:  # handle all eceptions
            #     print('Error', e)
            #     print('general')

            # try:
            #     with open(friends_file_path) as handler:
            #         added_friend_dict = json.load(handler)
            # if len(added_friend_dict[sign_in_user.username]) == 0:
            #     with open(friends_file_path, "a") as handler:
            #         json.dump({sign_in_user.username:[]}, handler)
            # else:
            #     sign_in_user.friends = added_friend_dict[sign_in_user.username]
            #     print(yes_no_menu(sign_in_user.set_friends, 'Add a Friend', usernames_list[entered_key4_1 - 1]))
            #
            #     added_friend_dict = {
            #         sign_in_user.username: sign_in_user.friends
            #     }
            #
            #     with open(friends_file_path, "a") as handler:
            #         json.dump(added_friend_dict, handler)
            #     break
        elif entered_key4_1 == 0:
            print('Returning to Previous Menu...')
            break
        else:
            print('Wrong Input! Please Try Again.')

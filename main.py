import datetime
import re

import pandas as pd
import pytz

import post

import comment

import sign_in

from Social_Network.profile import df_saved_prof_info
from Social_Network.sign_up import usernames_list

# CSV files path
auth_file_path = 'authentication_info.csv'
profile_path = 'profile_info.csv'
post_file_path = 'post_info.csv'
comment_file_path = 'comment_info.csv'





def print_list_index(list):
    for _ in range(len(list)):
        print(f'{_ + 1}) {list[_]}')


def yes_no_menu(method, action_name):
    while True:
        entered_key = input(f'\n***Do You Want to {action_name}?(Y/N)\n')
        if entered_key in ['y', 'Y']:
            return method()
            break
        elif entered_key in ['n', 'N']:
            return None
            break
        else:
            print('Wrong Input!Try Again Please')

def get_profile_data():
    input_name = input('Enter Name:\n')
    input_family = input('Enter family:\n')
    phone_frmt = '^09[\d]{9}$'
    while True:
        input_phone = input('Enter Your Phone Number:\n')
        if not re.search(phone_frmt, input_phone):
            print('Phone Number Format is not valid')
        else:
            input_phone = input_phone
            break

    email_frmt = '^[\w]+@[\w]+\.\w+$'
    while True:
        input_email = input('Enter email:\n')
        if not re.search(email_frmt, input_email):
            print('Email Format is not valid')
        else:
            input_email = input_email
            break

    input_bio = input('Enter bio:\n')
    return [input_name, input_family, input_phone, input_email, input_bio]

def save_data(path, attr_ls, header_ls):
    df_save = pd.DataFrame([attr_ls], columns=header_ls)
    df_save.to_csv(path, mode='a', index=False, header=False)


#
# print('**************************************************\n******Welcome to Social Network Application******'
#       '\n**************************************************\n')
# while True:
#     selection = input('1) Sign up\n2) Sign in')
#     if selection == '1':
#         print(sign_up.sign_up())
#     elif selection == '2':
sign_in_user = sign_in.sign_in()
sign_in_user.set_profile()
sign_in_profile = sign_in_user.profile
while True:
    entered_key = input('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                        'Select an Action below:\n'
                        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                        '1)Show/Edit Your Profile\n'
                        '2)Show/Edit Your Posts\n'
                        '3)Show friends List/Profile\n'
                        '4)Follow a User\n'
                        '5)Show Users Post/Comment\n'
                        '6)Send New Post\n'
                        'Press "0"(zero) to sign out\n\n')
    if entered_key == '0':  # sign out
        sign_in_user = None
        print('***You Signed out Successfully.\n See You Next Time')
        break
    if entered_key == '1':
        # Show Profile
        print(f'~~~Your Profile~~~\n{sign_in_user.profile}')
        # Edit Profile
        input_prof_data= yes_no_menu(get_profile_data, 'Edit Profile')
        if input_prof_data != None: # check whether user fill the profile or not
            sign_in_user.profile.edit_profile(*input_prof_data)
            # save data in csv file named "authentication.csv"
            save_data(profile_path,[sign_in_user.username, sign_in_user.profile.name, sign_in_user.profile.family,
                         sign_in_user.profile.phone, sign_in_user.profile.email, sign_in_user.profile.bio],
            ['Username', 'Name', 'Family', 'Phone', 'Email', 'Bio'] )


    if entered_key == '2':
        if len(sign_in_user.posts) != 0:
            # Show Posts
            print_list_index(sign_in_user.posts)
            # Edit Posts
            input_post_index = input('Select a Post to edit (Enter the number):\n')
            sign_in_user.posts[input_post_index-1].edit_post(input('Enter New Content:\n'))
        else:
            print('You have No Post Yet!')

    if entered_key == '3':
        while True:
            print('_______________\n***Your Friends List:')
            print_list_index(sign_in_user.friends)  # show all friends listed with index to choose from
            while True:
                entered_key3 = int(
                    input('\n\n***Enter a Friend Number to show the profile (Press "0" to Return):***\n\n'))
                if entered_key3 in range(1, len(sign_in_user.friends) + 1):
                    print('Returning to Previous Menu...')
                    break
                elif entered_key3 == 0:
                    friend_username = (sign_in_user.friends[entered_key3 - 1])
                    print('~~~Friend Profile~~~')
                    print(dict(df_saved_prof_info.loc[friend_username]))
                    break
                else:
                    print('Wrong Input! Please Try Again.')
    if entered_key == '4':  # See Users list and their profiles then Follow a User
        print_list_index(usernames_list)  # print users username as a list with index
        while True:
            entered_key4_1 = int(
                input('\n\n***Choose a User to See Profile (Enter a Number): (Press "0" to Return):***\n\n'))
            if entered_key4_1 in range(1, len(usernames_list) + 1):
                selected_user_username = (usernames_list[entered_key4_1 - 1])
                print(f'{selected_user_username}~~~ Profile~~~')
                print(dict(df_saved_prof_info.loc[selected_user_username]))
                break
            elif entered_key4_1 == 0:
                print('Returning to Previous Menu...')
                break
            else:
                print('Wrong Input! Please Try Again.')

        # added_friend = usernames_list[entered_key4_1 - 1]
        # sign_in_user.friends.append(added_friend)
        # print(f'~~~{added_friend} is Now Your friend!')
    if entered_key == '5':
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
                            selected_post = post.Post(usr_post_id_list[selected_post_index - 1], sign_in_user)
                            print(selected_post.set_comment())
                            break
                        elif entered_key5_1 in ['n', 'N']:
                            break
                        else:
                            print('Wrong Input!Try Again Please')
                    break

    if entered_key == '6':
        user_post = post.Post(sign_in_user.username)
        user_post.post_content = input('Write Post Content:\n')
        user_post.timestamp = set_timestamp()
        print(user_post.new_post(sign_in_user.post_num))
        save_data(post_file_path,
                  [user_post.post_id, user_post.post_content, user_post.timestamp, user_post.comment_num],
                  ['Post_ID', 'Content', 'Timestamp', 'NumOfComment'])

        # if entered_key == '5':
    # if entered_key == '5':/
    # while True:
    #     entered_key_5 = input('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    #                            'What Do You Want to Do? Enter a Number Please:\n'
    #                            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    #                            '1)Sent New Comment\n'
    #                            '2)Edit Comment\n'
    #                            '3)Delete Comment\n'
    #
    #     if entered_key_5 == '1':
    #     if entered_key_5 == '2':
    #     if entered_key_5 == '3':

    if entered_key == '6':
        sign_in_user_post = post.Post(sign_in_user.username)
        sign_in_user.posts.append(sign_in_user_post)
        sign_in_user_post.new_post(len(sign_in_user.posts))

    if entered_key == '7':
        pass
    # if entered_key == '8':
    #
    #    while True:
    #        input('Select a User to Follow:\n')
    #         [for user in sign_up.usernames_list:print(use)]
    # # if entered_key == '8':
    # if entered_key == '8':
    # if entered_key == '8':
    # if entered_key == '8':
    #
    # if entered_key == '6':
    #     pass
    # if entered_key == '6':
    #     pass

# break
# print(sign_up.df_saved_auth_info.loc[input_username])

# else:
# print('Wrong Input!')

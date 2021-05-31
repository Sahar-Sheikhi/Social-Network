import logging

import profile

from sign_in import sign_in

from sign_up import sign_up

import functions


from Social_Network.csv_functions import read_file_index, read_file_row


def signing_menu():
    """
    Menu for user to choose between register or log in
    return a user obj which will be used as sign_in user in main_menu
    """
    while True:
        try:
            selection = input('******** What Do You Want to do ********\n1) Sign up\n2) Sign in\n________________\n')
            assert selection in ['1', '2']
            if selection == '1':
                print('Your Selection = Sign_up\nTo Register Please Enter Your Username and Password.\n')
                print(sign_up())
                signing_menu()
            elif selection == '2':
                print('Your Selection = Sign_in\n')
                sign_in_user = sign_in()
                # check whether it is the first log_in or not
                if sign_in_user.username not in read_file_index(functions.profile_path, 'Username'):
                    # create a Profile for the new user
                    sign_in_user.set_profile()
                else:
                    sign_in_user_prof_attr_list = list(read_file_row(functions.profile_path,
                                                                     'Username', sign_in_user.username,''))
                    sign_in_user.profile= profile.Profile(*sign_in_user_prof_attr_list)
                    print(sign_in_user.profile)
                return sign_in_user

        except AssertionError:
            print('Invalid Input Please try again')


def action_menu(user_obj):
    """
    Menu for signed_in user to choose its desired action
    """
    while True:
        try:
            entered_key = input('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                                'Select an Action below:\n'
                                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                                '1)Show/Edit Your Profile\n'
                                '2)Show/Edit Your Posts/Send New Post\n'
                                '3)Show friends List/Profile/Unfollow\n'
                                '4)Follow a User(Show all Users)\n'
                                '5)Show Users Post/Comment/Send or Edit Comment\n'
                                '6)Send New Post\n'
                                'Press "0"(zero) to sign out\n\n')
            assert entered_key in ['0','1','2','3','4','5','6']
            if entered_key == '0':  # sign out
                user_obj = None
                print('***You Signed out Successfully.See You Next Time***\n\n')
                logging.info('Successful Logout')
                main_menu()
            if entered_key == '1':  # show/edit Profile
                # Show Profile
                functions.show_prof(user_obj)

                # Edit Profile
                functions.edit_prof(user_obj)

                #change Password
                functions.change_pass(user_obj)



            if entered_key == '2':  # show and edit post
                functions.show_edit_post(user_obj)

            if entered_key == '3':  # see friend and profile and unfollow a friend
                functions.see_friend_profile(user_obj)

            if entered_key == '4':  # See Users list and their profiles then Follow a User
                functions.follow(user_obj)

            if entered_key == '5':  # Show Users Post/Comment/Send or Edit Comment
                functions.users_post_comment_show_edit(user_obj)

            if entered_key == '6':  # send new post
                functions.send_post(user_obj)

        except AssertionError:
            print('Invalid Input')


def main_menu():
    signed_in_user = signing_menu()
    action_menu(signed_in_user)

import sign_in

import menu
from Social_Network import sign_up

print('**************************************************\n******Welcome to Social Network Application******'
      '\n**************************************************\n')
print('__________\ntest case:\nusername = sahar\npassword = 123\n__________\n')

while True:
    selection = input('1) Sign up\n2) Sign in\n________________')
    if selection == '1':
        print(sign_up.sign_up())
    elif selection == '2':
        sign_in_user = sign_in.sign_in()
        sign_in_user.set_profile()
        sign_in_profile = sign_in_user.profile
        while True:
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
            if entered_key == '0':  # sign out
                sign_in_user = None
                print('***You Signed out Successfully.\n See You Next Time')
                break
            if entered_key == '1':  # show/edit Profile
                menu.show_edit_profile(sign_in_user)

            if entered_key == '2':  # show and edit post
                menu.show_edit_post(sign_in_user)

            if entered_key == '3':  # see friend and profile
                menu.see_friend_profile(sign_in_user)

            if entered_key == '4':  # See Users list and their profiles then Follow a User
                menu.follow_unfollow(sign_in_user)

            if entered_key == '5':  # Show Users Post/Comment/Send or Edit Comment
                menu.users_post_comment_show_edit(sign_in_user)

            if entered_key == '6':  # send new post
                menu.send_post(sign_in_user)
    else:
        print('Wrong Input!')

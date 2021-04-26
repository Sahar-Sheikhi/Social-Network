from log_in_out import *


# test case
user1 = User('woody', '123', 9126129808, 'sahar@gmail.com', 'I am devops.', None, 'sahar', 'sheikhi')
# username = woody
# password = 123

post1=Post('first post')
username_list.append(user1.username)
password_list.append(user1.password)
user_obj_dict[user1.username] = user1
user_pass_dict[user1.username] = user1.password

sign_up_in()
if len(logged_in_user)!=0:
    logged_in_user = logged_in_user[0]
while True:
    menu_selection = input('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                           'Welcome:\n'
                           '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                           '1)show your profile\n'
                           '2)show posts\n'
                           '3)show friends\n'
                           '4)send a new post\n'
                           '5)Show a friend profile\n'
                           '6)show a friend posts\n'
                           'Enter o to log out')
    if menu_selection == 'o':
        print('***You are logged out.')
        sign_up_in()
    if menu_selection == '1':
        print(logged_in_user.show_profile())
    if menu_selection == '2':
        logged_in_user.posts

    if menu_selection == '3':
        print(logged_in_user.set_friends())
#     if menu_selection == '1':
#     if menu_selection == '1':
#     if menu_selection == '1':

print(post1.show_post())
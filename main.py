import profile
import sign_in
import sign_up
import user

# test case
# user1 = User('woody', '123', 9126129808, 'sahar@gmail.com', 'I am devops.', None, 'sahar', 'sheikhi')
# username = woody
# password = 123


print('**************************************************\n******Welcome to Social Network Application******'
      '\n**************************************************')
while True:
    selection = input('1) Sign Up\n2) Sing in')
    if selection == '1':
        print(sign_up.sign_up())
    if selection == '2':
        sign_in_user = sign_in.sign_in()
        break
while True:
    menu_selection = input('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                           'Select an Action below:\n'
                           '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                           '1)show your profile\n'
                           '2)show posts\n'
                           '3)show friends\n'
                           '4)send a new post\n'
                           '5)Show a friend profile\n'
                           '6)show a friend posts\n'
                           'Enter o to sign out')
    if menu_selection == 'o':
        print('***You are logged out.')
        break
    if menu_selection == '1':
        print(profile)
    if menu_selection == '2':
        print(sign_in_user.posts)

    # if menu_selection == '3':
    #     print(logged_in_user.set_friends())
#     if menu_selection == '1':
#     if menu_selection == '1':
#     if menu_selection == '1':

    # break

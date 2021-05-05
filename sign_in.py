import hashlib

import sign_up

import user


def sign_in():
    """
    This function does sign in or sign up
    """
    while True:
        input_username = input('Enter username:\n')
        input_password = input('Enter password:\n')
        hash_password = hashlib.sha256(input_password.encode('utf8')).hexdigest()

        # with open(sign_up.file_path, 'a', newline='') as handler:
        #     csv_writer = csv.writer(handler)
        #     csv_writer.writerows(new_user_info)

        if input_username not in sign_up.username_list:
                # or sign_up.df_saved_info.loc[input_username] != hash_password:
            print('username or password wrong plz try again')
        else:
            print(f'*** Dear {input_username}:\n You Have logged in Successfully!\n')
            break
    return user.User(input_username, input_password,None,None,None)




# print(sign_in())

import pandas as pd


def save_data(path, attr_ls, header_ls):
    """
    Save data to a csv file
    path:file path
    attr_list=input data
    header_ls=headers list for input data
    """
    df_save = pd.DataFrame([attr_ls], columns=header_ls)
    df_save.to_csv(path, mode='a', index=False, header=False)


def read_file_row(path, index_name, index_value, not_found_msg):
    """
    read a csv file by given index_name
    path:file path
    index: represents dataframe index name(str)
    return the rest of the row in csv whose index is index_name
    """

    df_read = pd.read_csv(path, index_col=index_name)
    if index_value in df_read.index:
        return df_read.loc[[index_value]]
    else:
        return f'{not_found_msg}'
# print(list(read_file_row('post_info.csv', 'Post_ID','woody_1','')))

def edit_data(path, index_name, index_value, header_name_ls, new_value_ls):
    """
    This Function updates only a row in csv based on given index_name
    header_name_ls: represents list of headers
    new_value_ls: represents list of new values
    """
    df_read = pd.read_csv(path, index_col=index_name)
    for h in range(len(header_name_ls)):
        df_read.loc[index_value, header_name_ls[h]] = new_value_ls[h]
    df_read.to_csv(path, mode='w', index=True, header=True)


def read_file_cell(path, index_name, index_value, header_name, msg):
    """
    This Function read a cell from csv file
    path: file path
    index_name : row name
    header_index: column name
    msg : string message appears when there is no such cell in the file
    """
    df_read = pd.read_csv(path, index_col=index_name)
    if index_value in df_read.index:
        return df_read.loc[index_value, header_name]
    else:
        return f'{msg} !'


# def update_cell(path, index_name, index_value, header_name, new_cell_value, msg):
#     df_read = pd.read_csv(path, index_col=index_name)
#     old_cell_value=df_read.loc[index_value, header_name]
#     print(old_cell_value)
#     if index_value in df_read.index:
#         # if df_read.loc[index_value, header_name] ==
#         df_read.replace(to_replace=[old_cell_value], value= int(new_cell_value), inplace= True)
#         print(df_read)
#         # df_read.to_csv(path, mode='w')
#     else:
#         return f'{msg}!'


# update_cell('post_info.csv', 'Post_ID', 'sahar_1', 'NumOfComment',71, '')


def read_file_index(path, index_name):
    """
    read a csv file by given index_name
    path:file path
    index: represents dataframe index name(str)
    return a list of index
    """
    df_read = pd.read_csv(path, index_col=index_name)
    return list(df_read.index)

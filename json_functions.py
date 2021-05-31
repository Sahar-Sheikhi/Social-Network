import json


def read_json_file(path, key):
    """
    This Function get a json file path and a key and return the value as a list
    path: represent a json file path
    key: represent a key in dict saved in json file
    return value of key which is a list
    """
    try:
        with open(path) as handler:
            read_dict = json.load(handler)
            return read_dict[key]
    except FileNotFoundError as fnferr:
        print(fnferr)
    except:
        return False


def write_json_file(path, key, value):
    """
    This Function add a key,value to json file

    """
    try:
        with open(path) as handler:
            read_dict = json.load(handler)
            if key in read_dict:
                read_dict[key].append(value)
                with open(path, 'w') as handler:
                    json.dump(read_dict, handler)
            else:
                read_dict[key] = [value]
                with open(path, 'w') as handler:
                    json.dump(read_dict, handler)

    except FileNotFoundError as fnferr:
        print(fnferr)
    except:
        return False

def edit_json(path, key, new_value_list):
    with open(path) as handler:
        read_dict = json.load(handler)
    for k,v in read_dict.items():
        if k == key:
            # del read_dict[k]
            read_dict[key] = new_value_list
    with open(path, 'w') as handler:
        json.dump(read_dict, handler)

# edit_json('friends_info.json', "woody", ["rar"])
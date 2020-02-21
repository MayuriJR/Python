#find and move file that has some special character

#Standard libary
import os
import shutil
import re

def find_file (src_path, file_type_index, key_str, path_list):
    """
    find file that endswith "index" and contain "key_str" in it's name
    """
    file_list = os.listdir(src_path)
    for file_name in file_list:
        file_abs_path = os.path.join(src_path, file_name)
        if os.path.isdir(file_abs_path):
            find_file(file_abs_path, file_type_index, key_str, path_list)
        elif file_name.endswith(file_type_index) and os.path.isfile(file_abs_path):
            if _is_contain_str(file_name, key_str):
                path_list.append(file_abs_path)

def move_file(path_list, des_path) :                              #copy pdf file to destination file
    "move file to destnation path"
    print("total : %d  file" % len(path_list))
    sum = 1
    try :
        os.mkdir(des_path)
    except Exception as e:
        print(e)
    for file_path in path_list:
        try :
            shutil.copy(file_path, des_path)
            print("{0} successfully  >>>  total:{1} " . format(sum, len(path_list)))
            sum += 1
        except Exception as e:
            print(e)

def _is_contain_str(file_name, key_str):
    standard_key_str = key_str 
    pattern = re.compile(standard_key_str, re.I)
    result = pattern.findall(file_name,)
    if len(result) > 0:
        return True
    return False

if __name__ == "__main__":
    src_path = "./Ws"
    file_type_index = ".xlsx"
    key_str_list = ["4mjc2", "4mjc3", "12mjc1", "12mjc2"]
    for key_str in key_str_list:
        path_list = []
        find_file(src_path, file_type_index, key_str, path_list)
        dest_path = "./%s" % (key_str)
        move_file(path_list, dest_path)

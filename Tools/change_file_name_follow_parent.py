# Change file name recursively by adding it's parent file name at begaining

# Standard libary
import os
import shutil

def change_file_name(src_path, Name, index):
    file_name_list = os.listdir(src_path)
    for file_name in file_name_list:
        file_abs_path = os.path.join(src_path, file_name)
        if os.path.isdir(file_abs_path):
            change_file_name(file_abs_path, file_name, index)
        elif file_name.endswith(index) and os.path.isfile(file_abs_path):
            name_after_modify = Name + file_name
            file_abs_path_after_modify = os.path.join(src_path, name_after_modify)
            os.rename(file_abs_path, file_abs_path_after_modify)

if __name__ == "__main__":
    src_path = "./Ws"
    index = ".xlsx"
    change_file_name(src_path, "Ws", index)

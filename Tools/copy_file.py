#find and move file that has some special character

#Standard libary
import os
import shutil


file_list = []
def find_file (src_path, index):
    """
    find file endswith "index"
    """
    file_content = os.listdir(src_path)
    for file in file_content:
        file_abs_path = os.path.join(src_path, file)
        if os.path.isdir(file_abs_path):
            find_file(file_abs_path, index)
        elif file.endswith(index) and os.path.isfile(file_abs_path):
            file_list.append(file_abs_path)

def move_file(des_path) :                              #copy pdf file to destination file
    print("total : %d  file"%len(file_list))
    sum = 1
    try :
        os.mkdir(des_path)
    except Exception as e:
        print(e)
    for file in file_list:
        try :
            shutil.copy(file, des_path)
            print("{0} successfully  >>>  total:{1} ".format(sum, len(file_list)))
            sum += 1
        except Exception as e:
            print(e)

src_path = r"C:\Users\Administrator\Desktop\precipitation"
dest_path = r"C:\Users\Administrator\Desktop\temp"
index = ".txt"
find_file(src_path, index)
move_file(dest_path)
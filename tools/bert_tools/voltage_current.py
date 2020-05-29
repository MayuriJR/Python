"""conver current-voltage data from txt type into  xlsx type"""
#need modify

#Standard libary
import os
import time
#Third part package
from pandas import DataFrame

def get_file_info(doc_path):
    file_list = [x for x in os.listdir(doc_path)]
    txt_file_paths = []
    for file in file_list:
        txt_file_path = os.path.join(doc_path, file)
        txt_file_paths.append(txt_file_path)
    return file_list, txt_file_paths

def read_txt_file(file_path):
    v_c = {}
    useful_data = []
    with open(file_path, "rb") as f:
        all_data = f.readlines()
        for i,item in enumerate(all_data):
            if (i % 2) == 1:
                useful_data.append(item.decode("utf-8"))
            else:
                pass
        for i, item in enumerate(useful_data):
            key_name1 = "%d_avoltage"%i
            key_name2 = "%d_current"%i
            v_list = []
            c_list =[]
            if (len(useful_data[0].split(",")) - 1 ) % 2 == 0 :
                topNum = len(useful_data[0].split(","))
            else :
                topNum = len(useful_data[0].split(",")) - 1
            for j, item in enumerate(useful_data[0].split(",")[1: topNum]):
                if (j % 2) == 0:
                    v_list.append(item)
                else:
                    c_list.append(item)
            v_c[key_name1] = v_list
            v_c[key_name2] = c_list
        f.close()
    return v_c

def to_excel(dest_path, dict={}):
    df = DataFrame(dict)
    df.to_excel(dest_path)

def get_dest_path(dest_path, txt_file_names=[]):
    dest_file_names = []
    for txt_file_name in txt_file_names:
        temp_path = os.path.join(dest_path, txt_file_name)
        real_path = temp_path[:-3] + "xlsx"
        dest_file_names.append(real_path)
    return dest_file_names

def main(doc_path, dest_path):
    try:
        os.mkdir(dest_path)
    except Exception as e:
        print(e)
    txt_file_names, txt_file_paths = get_file_info(doc_path)
    print("total " + str(len(txt_file_names)) + " files")
    to_paths = get_dest_path(dest_path, txt_file_names)
    for i,txt_file_path in enumerate(txt_file_paths):
        content = read_txt_file(txt_file_path)
        to_excel(to_paths[i], content)
        print(str(i + 1) + "complete")


if __name__ == "__main__":
    doc_path = r"C:\Users\Administrator\Desktop\Data"
    dest_path = r"C:\Users\Administrator\Desktop\ExperimentData"
    main(doc_path, dest_path)
    print("Done")
"""author : mayuri"""

# Standard library
import os
import time

# Third party package
import pandas as pd


def get_path(file_path):
    """Return excel file path
    """
    # absolute path of all excel file
    file_abs_path = []
    ex_list = [x for x in os.listdir(file_path)]
    for item in ex_list:
        if item.endswith(".xlsx"):
            file_abs_path.append(os.path.join(file_path, item))
    return file_abs_path


def get_sheet_name(excel_path):
    """
    Return sheets names
    """
    df = pd.read_excel(excel_path, None)
    sheet_name_list = df.keys()
    sheet_names = [x for x in sheet_name_list]
    return sheet_names


def merge_excel(file_abs_path, sheet_names, out_filepath):
    """ Merge excel that has same sheet name
    """
    index = 0
    for sheet_name in sheet_names:
        print("working on :%s" % sheet_name)
        out_excel_path = os.path.join(out_filepath, sheet_name) + ".xlsx"
        writer = pd.ExcelWriter(out_excel_path, engine='openpyxl')
        all_data = []
        for excel_file in file_abs_path:
            try:
                _df = pd.read_excel(excel_file, sheet_name=sheet_name)
                check_name(sheet_name, _df, excel_file)
                for i in range(len(_df)):
                    all_data.append(list(_df.loc[i]))
                _df = None
            except Exception as e:
                print(e)
                continue
        if len(all_data) == 0:
            print("these sheets named {0} are all none".format(sheet_name))
            continue
        df = pd.DataFrame(all_data, columns=["date", sheet_name])
        df.to_excel(excel_writer=writer, sheet_name=sheet_name,
                    encoding="utf-8", index=False)
        print(sheet_name + " save successfully ！  total :%d ，this is %d"
              % (len(sheet_names), index))
        index += 1
        writer.save()
        writer.close()


def check_name(sheet_name, df, excel_file):
    column_name = df.columns[1]
    if sheet_name != column_name:
        print("{0} file occur error, it's column name should be {1}, "
              "but is {2}".format(excel_file, sheet_name, column_name))


def main(file_path, out_filepath):
    try:
        os.mkdir(out_filepath)
    except Exception as e:
        print(e)
    file_abs_path = get_path(file_path)
    print("total :" + str(len(file_abs_path)) + "file")
    sheet_names = get_sheet_name(file_abs_path[0])
    print("total:" + str(len(sheet_names)) + "sheets")
    merge_excel(file_abs_path, sheet_names, out_filepath)
    print("Done")


if __name__ == "__main__":
    in_file = r"C:\Users\Mayuri\Desktop\12mJC1"
    out_file = in_file + "out"
    start_time = time.time()
    main(in_file, out_file)
    ends_time = time.time()
    print("running time is " + str(ends_time - start_time))

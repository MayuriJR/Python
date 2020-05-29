"""author : mayuri"""

# Standard library
import os

# Third party package
import pandas as pd


def get_list(file_path):
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
    index = 1
    for sheet_name in sheet_names:
        print("working on :%s" % sheet_name)
        df = None
        out_excel_path = os.path.join(out_filepath, sheet_name) + ".xlsx"
        writer = pd.ExcelWriter(out_excel_path, engine='openpyxl')
        for excel_file in file_abs_path:
            try:
                _df = pd.read_excel(excel_file, sheet_name=sheet_name)
            except Exception as e:
                _df = None
                print(e)
                continue
            # first into this function
            if df is None:
                df = _df
            else:
                df = pd.concat([df, _df], join="outer", ignore_index=True)
        df.to_excel(excel_writer=writer, sheet_name=sheet_name, encoding="utf-8", index=False)
        print(sheet_name + " save successfully ！    total :%d ，this is %d" % (len(sheet_names), index))
        index += 1
        writer.save()
        writer.close()


def main(file_path, out_filepath):
    try:
        os.mkdir(out_filepath)
    except Exception as e:
        print(e)
    file_abs_path = get_list(file_path)
    print("total :" + str(len(file_abs_path)) + "file")
    sheet_names = get_sheet_name(file_abs_path[0])
    print("total:" + str(len(sheet_names)) + "sheets")
    merge_excel(file_abs_path,sheet_names, out_filepath)
    print("Done")


if __name__ == "__main__":
    in_file = r"C:\Users\Administrator\Desktop\B"
    out_file = in_file+ "Out"
    main(in_file, out_file)

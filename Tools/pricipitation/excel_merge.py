#author : mayuri
#Standard libary
import os

# Third part package
import pandas as pd

def get_list(filepath):
    """Return excel file path
    """
    exabs_path = []
    #list of all excel file
    ex_list = [x  for x in os.listdir(filepath)]
    for item in ex_list:
        if item.endswith(".xlsx"):
            exabs_path.append(os.path.join(filepath, item))
    return exabs_path

def get_sehet_name(excel_path):
    """
    Return sheets names
    """
    df = pd.read_excel(excel_path, None)
    sheet_names = df.keys()
    sheet_list = [x for x in sheet_names]
    return sheet_list

def merge_excel(exabs_path, sheet_list, outfilepath):
    """ Merge excel that has same sheet name
    """
    index = 1
    for sheetName in sheet_list:
        print("working :%s" % sheetName)
        df = None
        out_excel_path = os.path.join(outfilepath, sheetName) + ".xlsx"
        writer = pd.ExcelWriter(out_excel_path, engine='openpyxl')
        for excel in exabs_path:
            try:
                _df = pd.read_excel(excel, sheetname=sheetName)
            except Exception as e:
                print(e)
                _df = None
            # first into this fuction
            if df is None:
                df = _df
            else:
                df = pd.concat([df, _df], join="outer", ignore_index=True)
        df.to_excel(excel_writer=writer, sheet_name=sheetName, encoding="utf-8", index=False)
        print(sheetName + " save successfully ！ >>> total :%d ，this is %d" % (len(sheet_list), index))
        index += 1
        writer.save()
        writer.close()

def main(filepath, outfilepath):
    try:
        os.mkdir(outfilepath)
    except Exception as e:
        print(e)
    excel_abs_path = get_list(filepath)
    print("total :" + str(len(excel_abs_path)) + "file")
    sheet_list = get_sehet_name(excel_abs_path[0])
    print("total:" + str(len(sheet_list)) + "sheets")
    merge_excel(excel_abs_path, sheet_list, outfilepath)
    print("Done")

if __name__ == "__main__":
    filepath = r"C:\Users\Administrator\Desktop\B"
    outfilepath = filepath + "Out"
    main(filepath, outfilepath)

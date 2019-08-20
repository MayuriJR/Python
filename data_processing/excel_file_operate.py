import pandas as pd                      #use pandas to solve excel_file
import os
def filter_data(path):
    excel_list=[x for x in os.listdir(path)]        #list of all excel file
    real_path=os.path.join(path,excel_list[0])
    df_sheet=pd.read_excel(real_path,None)
    all_sheets=df_sheet.keys()
    sheet_list=[x for x in all_sheets]            #list of all sheets
    print(sheet_list)
    index=1
    for sheet_name in sheet_list:
        print("I am working with :%s     (︶︹︺)  "%sheet_name)
        df=None
        temp_dest_name=sheet_name
        dest_name="%s.xlsx"%temp_dest_name
        writer = pd.ExcelWriter(dest_name,engine='openpyxl')  #create a destnation file_name
        for xlsx_name in excel_list:
            real_xlsx_name="./%s/%s"%(path,xlsx_name)
            try: #when this file doesn't exist then set _df is None 
                _df = pd.read_excel(real_xlsx_name, sheetname=sheet_name)
            except Exception as e:
                print(e)
                _df=None
			else:
                if df is None:
                    df=_df
                else :
                    df = pd.concat([df,_df],join="inner", ignore_index=True) #join two excel into one
        df.to_excel(excel_writer=writer, sheet_name=sheet_name, encoding="utf-8", index=False) #purple is a paraments  like dic
        print(sheet_name + "save successfully ！total :%d ，this is %d。 ( ´･◡･` ) " % (len(sheet_list), index))
        index+=1
        writer.save()
        writer.close()
    print("successfully")
if __name__=="__main__":
    filter_data("./BTS_1")                           #which file to solve  abs_path or path is all ok

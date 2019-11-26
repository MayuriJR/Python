"""
this file used to delete error data in a excel list

"""
###libraries
#third part package
import csv

#read csv file
def read_and_filte(src_path):
    useful_data = []
    with open(src_path, "r") as f:
        csv_reader = csv.reader(f)
        for i, data in enumerate(csv_reader):
            if 0 == i:
                useful_data.append(list(data))
            else:
                if float(data[1]) > 17.00 and 9.4 > float(data[2]) > 8.9:
                    useful_data.append(list(data))
        f.close()
        return useful_data

# write to csv file
def tocsv(dest_path, useful_data):
    with open(dest_path, "w",newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(useful_data)
        print("write successfully")
        return None

src_path = r"C:\Users\Administrator\Desktop\TEST.csv"
dest_path = r"C:\Users\Administrator\Desktop\out.csv"
u_data = read_and_filte(src_path)
tocsv(dest_path, u_data)

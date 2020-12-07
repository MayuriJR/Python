# dig out data from offical grid txt tape data

#### Libraries
# Standard libary
import os
# Third-party package
import csv


# get gird position
def get_coordinate(x, y):
    _x_corner = 72
    _y_corner = 54
    x_information = float(x)                                    #
    y_information = float(y)
    row_index = int((_y_corner - y_information) / 0.5)
    column_index = int((x_information - _x_corner) / 0.5)
    return row_index, column_index


# get data from file in a given position
def get_data(row_index, column_index, src_path, file_list, string_index):
    time_stamps = []
    precipitation = []
    for file in file_list:
        time_stamps.append(file[string_index[0]: string_index[1]])
        file_abspath = os.path.join(src_path, file)
        with open(file_abspath, "r") as f:
            data_all = f.readlines()
            data_row_index = data_all[row_index + 6].split()
            precipitation.append(data_row_index[column_index])
        f.close()
    return time_stamps, precipitation


def get_time_water(fileInfo=[], precipitation=[]):
    year_precipitation = []
    for i,year in enumerate(fileInfo):
        year_precipitation.append([year, precipitation[i]])
    return year_precipitation


# write to csv file
def to_csvfile(dest_path, year_pricipitation=[]):
    try:
        with open(dest_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Time", "pricipitation"])
            writer.writerows(year_pricipitation)
            f.close()
    except Exception as e:
        print(e)


# main process
def main(src_path, dest_path, x, y, date_type="month"):
    info_x = x
    info_y = y
    if date_type == "month":
        string_index = [-10, -4]
    if date_type == "day":
        string_index = [-12, -4]
    file_list = [file for file in os.listdir(src_path)]
    row_index, column_index = get_coordinate(info_x, info_y)
    print("total:" + str(len(file_list)) + "data")
    print("row: " + str(row_index))
    print("column: " + str(column_index))
    time_stamps, precipitation = get_data(row_index, column_index, src_path, file_list, string_index)
    year_pricipitation = get_time_water(time_stamps, precipitation)
    to_csvfile(dest_path, year_pricipitation)
    print("successfully")


# test unit
if __name__ == "__main__":
    # x means longitude of position
    # y means altitude of position
    date_type = "month"
    src_path = r"C:\Users\Mayuri\Desktop\2000-2019"
    dest_path = r"C:\Users\Mayuri\Desktop\2000-2019data.csv"
    x = 109.48
    y = 36.6
    main(src_path, dest_path, x, y, date_type)
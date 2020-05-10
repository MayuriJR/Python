'''
This module can filter time-type data from a high dimension into a low
dimension by using average of data associated with time .
'''

###Libraries
#Standard libary
import os
import xlrd

#Third-party package
import pandas as pd


class DataFilter(object):
    # paraments : in_path ,  addr of csv file where you put them
    #paraments : out_path ,  addr of outcoame where you put filtered data
    def __init__(self, src_path, dest_path):
        self.src_path = src_path
        self.dest_path = dest_path

    def __getFileNames(self, src_path):
        f_names = []
        f_paths = []
        temp_paths = [x for x in os.listdir(src_path)]
        for file in temp_paths:
            if file.endswith(".xlsx"):
                f_paths.append(os.path.join(src_path, file))
        for item in temp_paths :
            if item.endswith(".xlsx"):
                f_names.append(item[:-5])
        return f_names, f_paths

    def __getTargetPath (self, tar_path, f_name):
        t_paths = []
        names = [f_name + "mean_h.xlsx", f_name + "mean_d.xlsx"]
        name1 = os.path.join(tar_path, names[0])
        name2 = os.path.join(tar_path, names[1])
        t_paths.append(name1)
        t_paths.append(name2)
        return t_paths

    def __getData(self, f_path):
        temp_content = xlrd.open_workbook(filename=f_path, encoding_override='gbk')
        filtered_data = []
        df = pd.read_excel(temp_content, engine='xlrd')
        # df = pd.read_csv(f_path, header=0)
        col_index = []
        for item in df.head():
            col_index .append(item)
        df.set_index(col_index[0])

        #change data type from string into datetime
        df.index = pd.to_datetime(df[col_index[0]])

        # DataFrame[index].isin['args'] get data that include args
        # ~ means that we get a inverse data from precess.
        try:
            df1 = df[~df[col_index[1]].isin([0])]
        except Exception as e:
            df1 = None
            print("this file : " + str(f_path) + " occur Exception")
            return None
        # principle of filter
        # df1=df[df['WD'] < 50]
        d_mean_h = df1.resample('H').mean().ffill()
        d_mean_d = df1.resample('D').mean().ffill()
        filtered_data.append(d_mean_h)
        filtered_data.append(d_mean_d)
        return filtered_data

    def __writeData(self, filtered_data, t_paths):
        for i, data in enumerate(filtered_data):
            # data.to_csv(t_paths[i], sep=",")
            data.to_excel(t_paths[i])

    def run(self):
        try:
            os.mkdir(self.dest_path)
        except Exception as e:
            print(e)
        f_names, f_paths = self.__getFileNames(self.src_path)
        print("file names:" + str(f_names))
        print("file path" + str(f_paths))
        for i, f_path in enumerate(f_paths):
            print("total: %d file, %d is processing" % (len(f_paths), i+1))
            sub_doc_path = os.path.join(self.dest_path, f_names[i]) #inner document path
            try:
                os.mkdir(sub_doc_path)
            except Exception as e:
                print(e)
            t_paths = self.__getTargetPath(sub_doc_path, f_names[i]) #inner file path

            # Avoid something wrong in read excel file, if wrong we across this file
            try:
                data = self.__getData(f_path)   
            except Exception as e:
                print(e)
                continue
            if None == data:
                continue
            self.__writeData(data, t_paths)
            print("%d file done" % (i+1))

import csv
import numpy as np
import pandas as pd

co_path = r"C:\Users\Administrator\Desktop\coefficent.xlsx"
data_path = r"C:\Users\Administrator\Desktop\slopeData.csv"
out_path = r"C:\Users\Administrator\Desktop\outSlopeData.xlsx"

def one_tovector(x):
    x_ary = np.array(x)
    x_ary = np.atleast_2d(x_ary)
    X = np.zeros([6, x_ary.shape[1]])
    data = x_ary[0]
    for i in range(6):
        array = np.array([np.math.pow(float(x), i) for x in data])
        array.astype(float)
        X[i] = array
    return X.astype(float)

df = pd.read_excel(co_path, header=None)
coe_ary = np.array(df)
np.asarray(coe_ary)

with open(data_path, "r") as f:
    all_data = []
    csv_reader = csv.reader(f)
    for data in csv_reader:
        temp = np.dot(coe_ary, one_tovector(data))
        all_data.append(temp.diagonal())
    f.close()

out_df = pd.DataFrame(all_data)
out_df.to_excel(out_path)
print("Done")

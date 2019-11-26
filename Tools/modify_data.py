import pandas as pd
import numpy as np
import sys

excel_path = r"C:\Users\Administrator\Desktop\Temp.xlsx"
out_path = r"C:\Users\Administrator\Desktop\out.xlsx"

df = pd.read_excel(excel_path)
array_data = np.array(df)
array_data = array_data[:,1:].astype(float)
means = []
for i in range(array_data.shape[1]):
    means.append(np.mean(array_data[:,i]))
print(means)
for item in array_data:
    for i in range(len(item)):
        if item[i] < means[i] - 3 or item[i] > means[i] + 3:
            item[i] =  np.random.uniform(means[i]-2, means[i]+2)
df = pd.DataFrame(array_data.tolist())
df.to_excel(out_path)
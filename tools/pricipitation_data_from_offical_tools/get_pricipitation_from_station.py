####Libraries
#Third-party library
'''
This file get pricipitation data from a given fixed-type file.
'''
from pandas import DataFrame

src_path = r"C:\Users\Administrator\Desktop\water.txt"
place_index = "52889"
dest_path = r"C:\Users\Administrator\Desktop\pricipitation{0}.xlsx".format(place_index)
print(dest_path)

pricipitation_wanted = []
with open(src_path, "r") as f:
    count = 0
    null_data_count = 0
    pricipitation = f.readlines()
    print(len(pricipitation))
    for i, item in enumerate(pricipitation) :
        data = item.split()
        if 0 == len(data) :
            print("{0} row is null".format(i))
            null_data_count += 1
            continue
        elif place_index == data[0]:
            time = "{0}-{1}-{2}".format(data[1],data[2],data[3])
            count += 1
            if int(data[-1]) > 20000:
                pricipitation_wanted.append([time, 0])
            else:
                pricipitation_wanted.append([time, float(data[-1])/10])
    f.close()

df = DataFrame(pricipitation_wanted)
df.to_excel(dest_path)
print("total {0} null data".format(null_data_count))
print("total {0} data".format(count))
print("Done")
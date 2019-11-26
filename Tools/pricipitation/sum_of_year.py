#program precipitation data distrbuted in month to year.
#author :mayuri

#Third part package
import csv
data = []
with open(r"C:\Users\Administrator\Desktop\data_ld.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)
print(data)

years = []
precipitation = []
count = 0
for item in data:
    count += 1
    if 1 == count:
        continue
    year = item[0][0:4]
    years.append(year)
    water = float(item[1])
    precipitation.append(water)

year_water = {}
for i,year in enumerate(years):
    if year not in year_water:
        year_water[year] = precipitation[i]
    else:
        year_water[year] += precipitation[i]

with open(r"C:\Users\Administrator\Desktop\precipitation_ld1975.csv", "w", newline="") as csv_f:
    writer = csv.writer(csv_f)
    writer.writerow(["year", "precipitation"])
    for item in year_water:
        temp = [item, year_water[item]]
        writer.writerow(temp)

print("successfully")


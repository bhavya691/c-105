import math
import statistics
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
total = 0
for x in data:
    total+=int(x)
mean = total/len(data)
squared_list = []
for n in data:
    a = int(n) - mean
    a = a ** 2
    squared_list.append(a)
sum = 0
for i in squared_list:
    sum+=i
result = sum/(len(data)-1)
stdev = math.sqrt(result)
print(stdev)
data1 = [60,61,65,63,98,99,90,95,91,96]
print(statistics.stdev(data1))
import csv
import math

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    data = file_data[0]

def mean(data):
    n = len(data)
    total = 0

    for i in data:
        total += int(i)

    mean = (total/n)
    return mean

square_list = []
for j in data:
    a = int(j)-mean(data)
    a = a**2
    square_list.append(a)

sum = 0
for k in square_list:
    sum += int(k)

result = sum/(len(data)-1)
std = math.sqrt(result)

print("Standard Daviation-> ", std)

q = input("You Can Quit Now")
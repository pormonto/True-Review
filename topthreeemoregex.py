
import sys
import os
import pickle
import re

#=== Input File handling area ...
print("Which prediction.json to find top three: ")
input_file = input()

with open(f"{input_file}.json", 'r') as fileNow:
    rawjson = fileNow.read()

#=== Output File handling area ...

new_file = open("result_02.txt", "w")




regex1 = r"\"name\":\s*\"(\S+)\","
regex2 = r"\"score\":\s*(\d+\.\d+)}"

names = re.findall(regex1, rawjson)
scores = re.findall(regex2, rawjson)

print("names: ", names)
print("scores: ", scores)

with open("result_02.txt", "w") as new_file:
    for name, score in zip(names, scores):
        tempStr = f"{name}: {score}\n"
        new_file.write(tempStr)

    
new_file.close()
import re

fname = input("Enter file: ")
if len(fname) < 1: fname = "regex_sum_174818.txt"

try:
    fhandle = open(fname)
except:
    print("The file {} does not exist".format(fname))
    quit()

l=[]
for line in fhandle:
    if re.findall('[0-9]+',line) == []: continue
    else:
        l.extend(re.findall('[0-9]+',line))
final = sum([int(i) for i in l])
print(final)

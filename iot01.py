import os
#open file 
filename = ("symbols.txt")
if not os.path.isfile(filename):
    print("Input file "+ filename+" does not exist!")
    exit(1)
file = open(filename, "r")

#read input and put them in dict
user_in = input("Input: ")
user_in = user_in.split(',')
list_in = {}
for i in user_in:
    i = i.split(':')
    list_in[i[0]] = i[1]
print(list_in)

#output start from here
for line in file:
    for c in line:
        if c in list_in:
            c = list_in[c];
            print(c, end='')
    print('')
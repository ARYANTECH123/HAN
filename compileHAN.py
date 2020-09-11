import time
import math

print("Static HAN 1.2")
print("Developed by AG")

#Set filepath to program(stored in a text file)
fe = open('', "r")

#Reading the file line by line
bc = fe.readlines()

print("Rading file...")
print("Done!")
print("Compiling..")

#Processing and Tokenizing the progeam before parsing
bc = [sub[ : -1] for sub in bc]
tk = [l.split() for l in bc]

#Symbol table for the program
var = {}

for line in tk:
    if(line[0] == 'let'):
        var[line[1]] = float(line[3])


print("Compilation complete! Running static HAN\n\n")

for i in range(0, len(bc)):
    line = tk[i]

    if(line[0] == 'let'):
        continue
    elif(line[0] == 'pr'):
        if(line[1][0] == '$'):
            print(var[line[1][1:]])
        else:
            print(bc[i][3:])
    elif(line[0] == 'add'):
        var[line[1][1:]] = var[line[3][1:]] + var[line[5][1:]]
    elif(line[0] == 'sub'):
        var[line[1][1:]] = var[line[3][1:]] - var[line[5][1:]]
    elif(line[0] == 'mul'):
        var[line[1][1:]] = var[line[3][1:]] * var[line[5][1:]]
    elif(line[0] == 'div'):
        var[line[1][1:]] = var[line[3][1:]] / var[line[5][1:]]

    
    elif(line[0] == 'end'):
        break
    else:
        continue

        

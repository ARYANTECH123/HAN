import time
import math

def interpret(s):
    if(s[0] != '$'):
       

        return float(s)
    else:
        return var[s[1:]]

def cond(line):
    statement = str(interpret(line[1])) + line[2] + str(interpret(line[3]))
    return eval(statement)

#Set filepath to program(stored in a text file)
file = open('./Examples/prime_test.txt', "r")

#Reading the file line by line
bc = file.readlines()

print("Running pyHAN 1.2 patch 1")

print("Reading file...")
print("Done!")
print("Compiling..")

#Processing and Tokenizing the progeam before parsing
bc = [sub[ : -1] for sub in bc]
bc = [value for value in bc if value != '']
        

tk = [l.split() for l in bc]

#Symbol table for the program
var = {}

for line in tk:
    if(line[0] == 'let'):
        var[line[1]] = float(line[3])

print("\nCompiled! Running... \n\n")

i = 0
count = 0
while(True):    
    line = tk[i]
    
    if(line[0] == 'pr'):
        if(line[1][0] == '$'):
            print(var[line[1][1:]])
        else:
            print(bc[i][3:])
    elif(line[0] == 'add'):
        var[line[1][1:]] = interpret(line[3]) + interpret(line[5])
    elif(line[0] == 'sub'):
        var[line[1][1:]] = interpret(line[3]) - interpret(line[5])
    elif(line[0] == 'mul'):
        var[line[1][1:]] = interpret(line[3]) * interpret(line[5])
    elif(line[0] == 'div'):
        var[line[1][1:]] = interpret(line[3]) / interpret(line[5])
    elif(line[0] == 'mod'):
        var[line[1][1:]] = interpret(line[3]) % interpret(line[5])
    elif(line[0] == 'inc'):
        var[line[1][1:]] += 1
    elif(line[0] == 'goto'):
        i = int(line[1]) - 2        #A quick note on goto. Lines are indexed from 1 by default.
                                    #If you want lines to be indexed from 0 instead, change th '-2' to '-1'
                                    #If you index lines from 1, counting down becomes easier.
    elif(line[0] == 'skipif'):
        if(cond(line)):
            i += int(interpret(line[4]))
    elif(line[0] == 'doif'):
        if(not(cond(line))):
            i += int(interpret(line[4]))

#    elif(line[0] === ''):
        
    elif(line[0] == 'end'):
        break
    else:
        count += 1
    i += 1


print('\n\n Execution complete')
        

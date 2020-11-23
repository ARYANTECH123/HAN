import time
import math

#This function allows use of variables and floating point numbers interchangably
def interpret(s):
    global var
    if(s[0] != '$'):
        return float(s)
    else:
        return var[s[1:]]

#Evaluates binary conditions in HAN syntax
def cond(line):
    statement = str(interpret(line[1])) + line[2] + str(interpret(line[3]))
    return eval(statement)

#Set filepath to program(stored in a text file)
file = open('./Examples/example.txt', "r")

#Reading the file line by line
bc = file.readlines()

#Compiler messages, trivial
print("Running pyHAN 1.3 patch 1")
print("Reading file...")
print("Done!")
print("Compiling..")

#Processing and Tokenizing the progeam before parsing
bc = [sub[ : -1] for sub in bc]
bc = [value for value in bc if value != '']
        

tk = [l.split() for l in bc]

#Symbol table for the program
var = {}

#Function table
func = {}

for line in tk:
    if(line[0] == 'let'):
        var[line[1]] = float(line[3])

for line in tk:
    if(line[0] == 'def'):
        var['in:'+line[1]] = 0
        var['out:'+line[1]] = 0
        func[line[1]] = tk.index(line)
tk.append(['end'])

print("\nCompiled! Running... \n\n")

i = 0
count = 0
callpoint = 0

inFunc = False
err = False

while(True):    
    line = tk[i]
    
    #General IO
    if(line[0] == 'pr'):
        if(line[1][0] == '$'):
            print(var[line[1][1:]])
        else:
            print(bc[i][3:])

    #Variable handling
    elif(line[0] == 'set'):
        var[line[1][1:]] = interpret(line[3])

    #Integer algebra
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

    #Function calls
    elif(line[0] == 'call'):
        callpoint = i
        n = func[line[1]]
        i = n
        infunc = True
    elif(line[0] == 'enddef'):
        if(infunc):
            i = callpoint - 1
        else:
            count += 1
    elif(line[0] == 'def'):
        blockEnd = bc[i:].index('enddef') - i
        i = blockEnd

    #Program flow control 
    elif(line[0] == 'goto'):
        i = int(line[1]) - 2        #A quick note on goto. Lines are indexed from 1 by default.
                                    #If you want lines to be indexed from 0 instead, change th '-2' to '-1'
                                    #Lines indexed from 1 make counting down easier, especially in editors like VScode and Notepad++

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


if(not err):
    print('\n\n Execution complete')
else:
    print("Oh no! A error")        

import time

def exec(s):

    if(s[0:2] == 'pr'):
        print(s[2:])

#Set filepath to program(stored in a text file)
file = open('animation.txt', "r")

#Reading the file line by line
bc = file.readlines()

print("Rading file...")
time.sleep(1)
print("Done!")
time.sleep(1.5)
print("Compiling..")
time.sleep(3)

bc = [sub[ : -1] for sub in bc]
    

print("Compiled! Running static HAN\n")
    
i = 0
line = bc[i]
    
while(True):
    line = bc[i]

    if(line == 'end'):
        break 
    elif(line[0:3] == 'goto'):
        i = line[5:]
    else:
        exec(line)
        i += 1

print("\n\n Done executing!")
        


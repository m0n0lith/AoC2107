#!/bin/python3
# input of 1122 gives (1+2)=3
# input of 976542319 gives 9
# pos1 = pos1 -> pos1.value
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', default='', required=True)
args = parser.parse_args()

fileList = args.file
print ('.:INPUT:.')
f = open(args.file)
inputStr = f.readline()
inputStr = inputStr.strip('\n')
print (inputStr+'\n')
inputList = []
#print(inputStr)
inputLen = len(inputStr)
#for i in inputStr:
#    inputList.append(inputStr[i])
result = 0
for char in inputStr:
    #print (char)
    inputList.append(int(char))

#inputList.append(inputList[0])
print('.:LIST:.', '\n', inputList, '\n')

for i in range(len(inputStr)-1):
    if inputList[i] == inputList[i+1]:
        result = result + inputList[i]
        #print('split result: ' + str(result))
    else:
        result = result

#print(inputList[-1])
#print(inputList[0])
if inputList[0] == inputList[-1]:
    result = result + inputList[-1]
else:
    print('not equle')
    result = result

print('Sum: ' + str(result))

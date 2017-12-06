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
inputLen = len(inputStr)
listDiv = inputLen/2
result = 0
inputList = list(inputStr)

print('.:LIST:.', '\n', inputList, '\n')

for i in range(len(inputStr)-1):
    keck = int(i + listDiv) % inputLen
    if int(inputList[i]) == int(inputList[keck]):
        result = result + int(inputList[i])
    else:
        result = result


#if int(inputList[0]) == int(inputList[-1]):
#    result = result + int(inputList[-1])
#else:
#    print('not equle')
#    result = result

print('Sum: ' + str(result))

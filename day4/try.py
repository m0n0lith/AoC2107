#!/bin/python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', default='', required=True)
args = parser.parse_args()

with open(args.file) as inFile:
    inData = inFile.read().strip().split('\n')

fileList = []
#fileList.append(inFile.read().splitlines())
#inputStr = inputStr.strip('\n')
for i in inData:
    myDict = {}
    for n in i.split():
        if not n in myDict:
            myDict[n] = 9
    print(myDict)
    count = len(i.split())
    if count == len(myDict):
        fileList.append(i)
    print(len(myDict),',',count)
print('Nr of valids: ',len(fileList))

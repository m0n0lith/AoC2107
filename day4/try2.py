#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', default='', required=True)
args = parser.parse_args()

with open(args.file) as inFile:
    inData = inFile.read().strip().split('\n')

fileList = []
listValue = ()
listKeys = ()
#fileList.append(inFile.read().splitlines())
#inputStr = inputStr.strip('\n')
for i in inData:
    myDict = {}
    for n in i.split():
        myDict[n] = len(n)
    listValue = list(myDict.values())
    listKeys = (list(myDict.keys()))
    for m in range(len(myDict.keys())-1):
        if listValue[m] == listValue[m+1]:
            for x in range(len(listKeys)):
                
            #print('samma ',len(n),'\n')
    #else:
    #    print(myDict)
    #print(listValue[])
print('Nr of valids: ')

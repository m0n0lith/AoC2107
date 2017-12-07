#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', default='', required=True)
args = parser.parse_args()

with open(args.file) as inFile:
    inData = inFile.read().strip().split('\n')

resList = list()
for i in inData:
    myDict = {}
    for n in i.split():
        part = ''.join(sorted(n))
        if not part in myDict:
            myDict[part] = 9
    count = len(i.split())
    if count == len(myDict):
        resList.append(i)

print('Nr of valids: ', len(resList))

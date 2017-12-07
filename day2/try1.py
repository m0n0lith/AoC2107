#!/usr/bin/python3.6
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', default='', required=True)
args = parser.parse_args()
with open(args.file) as inFile:
    inData = inFile.read().strip().split('\n')
lenData = len(inData)
#print(inData)
count = 0
for i in inData:
    newi = ''.join(i.split())
    sortData = sorted(newi)
    #print(sortData)
    print(int(sortData[0]))
    count = count + (int(sortData[-1]) - int(sortData[0]))
print(count)

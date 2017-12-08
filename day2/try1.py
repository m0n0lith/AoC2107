#!/usr/bin/python3.6
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', default='', required=True)
args = parser.parse_args()
count = 0
#results = list()
with open(args.file) as inFile:
    inData = inFile.read().strip().split('\n')
lenData = len(inData)
print(inData)
for m in inData:
    print('M: ', m)
    splitData = m.split('\t')
    print('SplitData: ',splitData)
    for i in m:
        results = list(map(int, splitData))
        #newi = int(splitData[0])
        sortData = sorted(results)
    print('SortData: ', sortData)
    count = count + (sortData[-1] - sortData[0])
    #print('sortdata-1:',sortData[-1],' minus ',sortData[0],' is ',(sortData[-1] - sortData[0]))
print(count)

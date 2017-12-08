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
    # Make it INT
    for i in m:
        results = list(map(int, splitData))
        sortData = sorted(results)
    print(sortData)
    for n in range(0, len(sortData)):
        for k in range(0,len(sortData)):
            if n==k:
                continue
            if sortData[n] % sortData[k] == 0:
                count += sortData[n]/sortData[k]
        #print(sortData[n])
        #print(sortData[n] % sortData[n]+1)
        print('Yes! ',sortData[n],'/',sortData[k],' = ',sortData[n]/sortData[k])
    #print('sortdata-1:',sortData[-1],' minus ',sortData[0],' is ',(sortData[-1] - sortData[0]))
print(count)

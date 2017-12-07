#!/usr/bin/python3.6
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', default='', required=True)
args = parser.parse_args()
with open(args.file) as inFile:
    inData = inFile.read().strip().split('\n')
lenData = len(inData)
#print(inData[-1])
listing = list()

for i in inData:
    for n in i:
        listing.append(n)
    print(listing)

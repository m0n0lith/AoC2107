#!/usr/bin/python3.6
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', default='input.txt', required=True)
args = parser.parse_args()
with open(args.file) as inFile:
    inData = inFile.read().strip().split('\n')
lenData = len(inData)
print(lenData)
start = int(inData[0])
move = int(0)
inData[0] = inData[0].replace(inData[0],'('+inData[0]+')')
atPos = int(0)
print inData.index('0')
#print('At pos: ','value: '+inData[0])

#!/bin/python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', default='', required=True)
args = parser.parse_args()

inFile = open(args.file)
#inputStr = inFile.readline()
fileList = []
fileList.append(inFile.read().splitlines())
#inputStr = inputStr.strip('\n')
myList = []
#print (inputStr)
print(fileList)

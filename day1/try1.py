#!/bin/python3
# input of 1122 gives (1+2)=3
# input of 976542319 gives 9
# pos1 = pos1 -> pos1.value
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('--file', '-f', default='', required=True)

fileList = args.file
print (fileList)


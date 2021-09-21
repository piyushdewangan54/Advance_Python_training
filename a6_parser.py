"""
N: number
? 0 or 1 arguments
* 0 or all argument
+ All or atleast one argument
"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--three',nargs=3)
parser.add_argument('--optional',nargs='?')
parser.add_argument('--all',nargs='*',dest='all')
parser.add_argument('--one-or-more',nargs='+')

print(parser.parse_args())

#run in terminal
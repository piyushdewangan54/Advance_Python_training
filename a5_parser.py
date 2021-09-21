import argparse

from configparser import ConfigParser

import shlex

parse = argparse.ArgumentParser(description="sample app",
                                fromfile_prefix_chars='@')
parse.add_argument('-a', action="store_true", default=False )
parse.add_argument('-b', action="store", dest='b')
parse.add_argument('-c', action="store", dest='c', type=int )

print(parse.parse_args(['@abc.txt']))
import argparse

parse = argparse.ArgumentParser(description="example")

parse.add_argument('-a', action="store_true", default= False )
parse.add_argument('-b', action="store", dest='b' )
parse.add_argument('-c', action="store", dest='c' )


print(parse.parse_args(['-a', '-b', 'piyush', '-c', '3']))

# run in terminal
import argparse

parse = argparse.ArgumentParser(description="test")

parse.add_argument('count', action="store", type  = int )
parse.add_argument('units', action="store" )



print(parse.parse_args())

# if you run it from here run button then it will throw error bcoz we havent put the parameters
# but arg parser is used in development purpose so we can give parameters through command line
# code in terminal --> python a2.py 3 inch
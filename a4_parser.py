import argparse

parse = argparse.ArgumentParser()

parse.add_argument('-s', action="store", dest = 'simple_value', help='store simple value' )
parse.add_argument('-c', action="store_const", dest = 'constant_value', const='100',
                   help='store constant value')
parse.add_argument('-t', action="store_true", default= False,
                   dest='boolen_switch', help='set a switch to true')
parse.add_argument('-f', action="store_false", default= False,
                   dest='boolen_switch', help='set a switch to false')
parse.add_argument('-a', action="append", dest = 'collection', default=[],
                    help='add repeated values to list' )
parse.add_argument('-A', action="append_const", dest = 'const_collection',
                  const='300', help='add different values to list' )

parse.add_argument('--version', action="version", version='1.0' )


result = parse.parse_args()
print('Simple value = ', result.simple_value)
print('constant_value =',result.constant_value)
print('boolen_switch =',result.boolen_switch)
print('collection =',result.collection)
print('const_collection =',result.const_collection)


# run in terminal
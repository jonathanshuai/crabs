import argparse

import crabs
from crabs import Crab

parser = argparse.ArgumentParser(description='Begin a crab show.')
parser.add_argument('quantity', type=int, help='How many crabs to invite.')
parser.add_argument('-f', '--friend', help='Name of a friend to call instead.')

args = parser.parse_args()


def main():
    crab = Crab(args.quantity)
    if args.friend is None:
        crab.begin_show()
    else:
        crab.invite_friends(args.friend)



# parser.add_argument('quantity', metavar='N', type=int, nargs='1',
#                     help='How many images to show')

# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')



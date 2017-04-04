#!/usr/bin/env python3
import sys, collections
def main(argv):
        try:
                duplicated = collections.Counter(argv[0])
                print(''.join({k: v for k, v in duplicated.items() if v > 1}.keys()))
        except:
                print('Usage: ./pyduplicate.py "You need to add "YOUR PHRASE HERE" after running python ./pyduplicate.py"\n')
                raise
if __name__ == "__main__":
#      print(sys.argv)
        main(sys.argv[1:])

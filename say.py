# import cowsay
import sys

# if len(sys.argv) == 2:
#     cowsay.trex("Hello "+ sys.argv[1])

from sayings import hello, goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])
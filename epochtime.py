# Script to convert a Epoch Time in UTC
#
# You can enter an argument from the command line in the call: ex, epochtime 1123654
# If there's no argument, scripts asks for it
#
# Output is in american format MM:DD:YY

import time
import sys

def conv(val):
    i = time.strftime('%m-%d-%Y %H:%M:%S', time.gmtime(int(val)))
    print(i, "UTC")

try:
    arg = int(sys.argv[1])
    d = conv(arg)

except:
    try:
        i = input("Insert Unix Time: ")
        d = conv(i)

    except:
        print("Not a valid argument")

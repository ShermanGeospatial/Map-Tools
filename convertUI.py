import os
import sys

os.system("pyuic5 -x " + sys.argv[1] + " -o " + sys.argv[2])
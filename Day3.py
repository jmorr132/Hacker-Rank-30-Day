#!/bin/python

import sys


N = int(raw_input().strip())

if N % 2 == 0 and N <=5:
    print "Not Weird"
elif N % 2 == 0 and N <= 20:
    print "Weird"
elif N % 2 == 0 and N > 21 :
    print "Not Weird"
else:
    print "Weird"
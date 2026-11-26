"""
number of bits of a number --> 2**N
"""

import sys

n = int(sys.stdin.readline())
MOD = 10**9 + 7

print(pow(2, n, MOD))

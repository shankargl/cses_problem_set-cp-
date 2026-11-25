"""
two sets of the same sum for give n from 1 to n  .
input:-
4
output:-
YES
2
1 4 
2 
2 3 
"""


import sys
input = sys.stdin.readline

n = int(input())

set1 = set()
set2 = set()

total = n * (n + 1) // 2

if total % 2 == 1:
    print("NO")
else:
    half = total // 2
    ans = 0
    i = n

    while ans < half:
        set2.add(i)
        ans += i

        new = half - ans

        if new > 0 and new <= n and new not in set2:
            set2.add(new)
            ans += new

        i -= 1

    for j in range(1, n + 1):
        if j not in set2:
            set1.add(j)

    print("YES")
    print(len(set1))
    print(*set1)

    print(len(set2))
    print(*set2)

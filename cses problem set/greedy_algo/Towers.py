'''
Q.You are given n cubes in a certain order, and 
your task is to build towers using them.
Whenever two cubes are one on top of the other,
the upper cube must be smaller than the lower cube.
You must process the cubes in the given order. 
You can always either place the cube on top of an existing tower, 
or begin a new tower. What is the minimum possible number of towers?

APPROCH:
We maintain a sorted array towers, containing the top cube of every tower.

For every incoming cube x:
1. Find the first tower whose top cube is strictly greater than x.
2. If found, place x on that tower (replace its top).
3. Otherwise, create a new tower.
Why choose the smallest top that is greater than x?

Because it keeps the remaining tower tops as small as possible, 
giving future cubes more opportunities to fit.

NOTE:
1. Lower Bound( IN PYTHON USE "from bisect import bisect_left")
Definition: Lower bound returns the index of the first element that is greater than or equal to (>=) the target.

2. Upper Bound(IN PYTHON USE "from bisect import bisect_right")
Definition: Upper bound returns the index of the first element that is strictly greater than (>) the target.

'''

from bisect import bisect_right

n = int(input())
arr = list(map(int, input().split()))

towers = []

for x in arr:
    idx = bisect_right(towers, x)

    if idx == len(towers):
        towers.append(x)
    else:
        towers[idx] = x

print(len(towers))
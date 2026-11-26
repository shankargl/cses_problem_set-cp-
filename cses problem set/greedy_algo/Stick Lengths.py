'''
There are n sticks with some lengths.
Your task is to modify the sticks so that each stick has the same length.
You can either lengthen and shorten each stick. 
Both operations cost x where x is the difference between the new and original length.
What is the minimum total cost?

'''
import sys
input = sys.stdin.readline

n = int(input())
arr=list(map(int,input().split()))
arr.sort()
mid=len(arr)//2

element=arr[mid]
cost=0
for i in arr:
    cost+=abs(i-element)
print(cost)

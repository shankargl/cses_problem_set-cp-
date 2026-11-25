'''
You are given an array of n integers. You want to modify the array so that it is increasing,
i.e., every element is at least as large as the previous element.
On each move, you may increase the value of any element by one. 
What is the minimum number of moves required?(greedy algorithm)
'''
import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

ans=0
for i in range(1,len(a)):
    if a[i]<a[i-1]:
        ans+=a[i-1]-a[i]
        a[i]=a[i-1]

print(ans)
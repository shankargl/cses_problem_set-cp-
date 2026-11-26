'''
There are n books, and Kotivalo and Justiina are going to read them all. 
For each book, you know the time it takes to read it.
They both read each book from beginning to end, 
and they cannot read a book at the same time. 
What is the minimum total time required?sample 

input 1
4
1 2 3 8
output 1
16

sample input 2
2
8 15
output 2
31

** if there is any element that is more than half sum of the array then the confusion start so 
   take take maximum of the array and multiply with 2 and take maximum b/w that and
    sum of all the elements.
    ans=\max(sum(arr),2\times max(arr))}
''' 
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
arr.sort()

max_time = arr[-1]

print(max(total, max_time * 2))

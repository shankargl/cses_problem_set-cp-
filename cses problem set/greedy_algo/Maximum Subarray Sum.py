'''
QUESTION:
Given an array of n integers, 
your task is to find the maximum sum of values in a contiguous, nonempty subarray.
ALGORITHM-->KADANSE ALGORITHM
'''

n = int(input())
arr = list(map(int, input().split()))

max_sum = arr[0]
current_sum = arr[0]

for i in range(1, n):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)

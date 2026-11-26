'''
In a movie festival n movies will be shown. 
You know the starting and ending time of each movie. \
What is the maximum number of movies you can watch entirely?
'''
import sys
input=sys.stdin.readline

N=int(input())
arr=[]
for _ in range(N):
    a,b=map(int,input().split())
    arr.append((a,b))

arr.sort(key=lambda x:x[1])

count=1
last_movie=arr[0][1]
for i in range(1,N):
    movie=arr[i]
    if movie[0]>=last_movie:
        count+=1
        last_movie=movie[1]

print(count)

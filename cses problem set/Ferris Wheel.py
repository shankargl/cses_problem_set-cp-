import sys
input=sys.stdin.readline

n,w=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort() 
#print(arr)
count=0
i=0
r=len(arr)-1
while i<=r:
    if arr[i]+arr[r]<=w:
        count+=1
        i+=1
        r-=1
    else:
        r-=1
        count+=1
print(count)
            

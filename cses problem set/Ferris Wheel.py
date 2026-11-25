import sys
input=sys.stdin.readline

n,w=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()
print(arr)
count=0
i=0
while i<len(arr):
    is_it=False
    if i+1<len(arr):
        total_weight=arr[i]+arr[i+1]
        if total_weight<=w:
            count+=1
            is_it=True
        else:
            count+=1

    else:
        count+=1

    if is_it:
        i+=2
    else:
        i+=1

print(count)
            

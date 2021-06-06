t=int(input())
n,k=map(int,input().split())
arr=list(map(int,input().split()))
k=k%n
while(k>0):
    t=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=t
    k-=1
print(*arr)

# Write your code here
n=int(input())
arr=list(map(int,input().split()))
ans=1
for i in range(len(arr)):
    ans=(ans*arr[i])%1000000007
print(ans)

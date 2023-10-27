m,d= map(int,input().split())
b=list(map(int,input().split()))

left = 1
right =10**9

while left <= right:
    mid =(left+right)//2
    count=0
    for i in range(m):
        if b[i] <= mid:
            count += 1
    if count == d:
        print(mid)
        break
    elif count < d:
        left = mid +1
    else:
        right =mid-1

if left > right:
    print(-1)

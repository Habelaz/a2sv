n= int(input())
a = list(map(int,input().split()))
count = 0 
answer = 0
for i in range(n):
    if a[i] % 2 == 1:
        count =1
    else:
        answer = 1
if answer and count:
    a.sort()
print(*a)

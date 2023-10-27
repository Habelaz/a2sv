n=int(input())
result=[]
for i in range(n):
    t=int(input())
    nl=list(map(int,input().split()))
    i=0
    j=1
    ans=[]
    while j < t:
        if abs(nl[j] - nl[i]) > 1:
            ans.append("NO")
        else:
            ans.append("YES")
        i += 1
        j += 1
    if "NO" in ans:
        result.append("NO")
    else:
        result.append("YES")
for i in result:
    print(i)

N = int(input())
ans = 0
for i in range(1,N+1):
    num = N//i
    a1 = i
    an = a1 + (num-1)*i
    ans += (num*(a1+an))//2
print(ans)

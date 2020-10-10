import sys
sys.setrecursionlimit(10000)

S = int(input())
mod = 10**9+7
ans = 1
cnt = 0

memo = [[-1]*2010 for i in range(2000)]

def f(r,bar):
    global cnt
    cnt += 1
    ans = 0
    if ((r//3)-1) < bar:
        memo[r][bar] = 0
        return 0
    if bar == 1:
        memo[r][bar] = (r-5)%mod
        return r-5
    else:
        if memo[r][bar] == -1:
            for i in range(r-3,5,-1):
                if memo[i][bar-1] == -1:
                    plus = f(i,bar-1)
                    memo[i][bar-1] = plus%mod
                    ans += plus
                else:
                    ans += memo[i][bar-1]
            memo[r][bar] = ans%mod
            return ans
        else:
            return memo[r][bar]
        return ans


if S <= 2:
    print(0)
else:
    N = S//3
    for i in range(1,N+1):
        ans += f(S,i)
        ans %= mod
    print(ans)

print(cnt)








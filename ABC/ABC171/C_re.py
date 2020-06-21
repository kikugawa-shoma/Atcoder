N = int(input())

s = 26
cnt = 1
while 1:
    if N <= s:
        break
    cnt +=1
    s+=26**cnt


N = N-s+26**cnt-1
r = [0]*cnt
ans = [0]*cnt
for i in range(cnt):
    r[i] = N % 26
    N //= 26
    ans[i] = chr(ord("a")+r[i])
ans.reverse()
print("".join(ans))




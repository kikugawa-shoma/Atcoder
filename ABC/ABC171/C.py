N = int(input())

base = 26

a = 26
cnt = 1
while 1:
    if N <= a:
        break
    else:
        a*=26
        cnt += 1
        

ans = []
num = []
for i in range(cnt):
    num.append(base**i)

for i in range(1,cnt+1):
    if i <= cnt-1:
        tmp = N-num[cnt-i]-1
        keta = tmp//base**(cnt-i)
        N -= (keta+1)*(base**(cnt-i))
        ans.append(chr(ord("a")+keta))
    else:
        ans.append(chr(ord("a")-1+N))
print("".join(ans))





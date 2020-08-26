N = int(input())
L = list(map(int,input().split()))
L.sort(reverse=True)

cnt = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            c = L[i]
            b = L[j]
            a = L[k]
            if c < a+b and c > b-a and a != b and b != c and c != a:
                cnt += 1
print(cnt)

N = int(input())
A = [int(a) for a in input().split()]
mod = 10**9+7
SUM = 0

maxA = max(A)
d = 0

while 1:
    if maxA < 2**d:
        break
    d += 1
#Aの最大値を表現するのに必要なbitの桁数を計算

BitSumB = 0
for i in range(d):
    tmp = 0
    for n in range(N):
        tmp += (A[n] >> i) & 1
        #各ビットの値を使いたいときは右シフトして１とのANDを使うと速い
    BitSumB += (2**i) * tmp * (N - tmp)


#XORの性質に着目。xorは繰り上げのない加算。

"""遅い
BitA = [[0]*d for _ in range(N)]
for i in range(N):
    BitA[i] = list(map(int, format(bin(A[i])[2:], '0>{}'.format(d))))

BitSumB = 0
for i in range(d):
    tmp = sum([BitA[j][i] for j in range(N)])
    BitSumB += 2 ** (d-i-1) * (tmp * (N - tmp))
    #BitSumB = BitSumB % mod
"""

print(BitSumB % mod)




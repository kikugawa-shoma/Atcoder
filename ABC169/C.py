import math
S = input().split()
A = int(S[0])
B = S[1]
B = B.rsplit(".")
B0 = B[0]
B1 = B[1]
B = int(B0)*100+int(B1)
ans = "000"+str(A*B)
n = len(ans)



print(int(ans[:n-2]))


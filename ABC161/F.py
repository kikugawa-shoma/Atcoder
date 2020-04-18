N = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

ans = 0
divisors = make_divisors(N)[1:]
ans += len(make_divisors(N-1))-1

for divisor in divisors:
        divided_N = N
        while 1:
            if divided_N%divisor!=0:
                break
            else:
                divided_N //=divisor
        if divided_N % divisor == 1:
            ans += 1
print(ans)

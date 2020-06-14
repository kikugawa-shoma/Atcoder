N = 3
A = [1000000, 999999, 999998]


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


mat = [1]
divs_set = set()
divs_powers = {}
tmp=[0]*len(A)
for j,a in enumerate(A):
    tmp[j] = factorization(a)
    for div in tmp[j]:
        if div[0] not in divs_set:
            divs_set.add(div[0])
            divs_powers[div[0]] = div[1]
        else:
            if divs_powers[div[0]] < div[1]:
                divs_powers[div[0]] = div[1]

all_dict = []
all_set = []
for i,t in enumerate(tmp):
    each_dict = {}
    each_set = set()
    for tt in t:
        each_dict[tt[0]] = tt[1]
        each_set.add(tt[0])
    all_dict.append(each_dict)
    all_set.append(each_set)

B = [1] * N
for i, a in enumerate(A):
    for k in divs_set:
        if k in all_set[i]:
            B[i] = B[i]*(k**(divs_powers[k]-all_dict[i][k]))
        else:
            B[i] = B[i]*(k**divs_powers[k])

print(int(sum(B)) % (10 ** 9 + 7))

L, R = map(int, input().split())

m = 2019

if R - L > 2100:
    print(0)
else:
    tmp_min = 2018
    for i in range(L, R):
        mod_i = i % m
        for j in range(i + 1, R+1):
            mod = (mod_i * j) % m
            if tmp_min > mod:
                tmp_min = mod
    print(tmp_min)

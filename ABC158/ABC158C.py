A, B = map(int, input().split())

for i in range(1, 1251):
    if int(i*0.08) == A and int(i*0.10) == B:
        print(i)
        break
else:
    print(-1)


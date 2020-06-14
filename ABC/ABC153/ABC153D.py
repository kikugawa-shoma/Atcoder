H = int(input())

power_2 = 1
i = 0
while power_2 <= H:
    power_2 = power_2 * 2
    i += 1

num = 0
for j in range(i):
    num += 2**j

print(num)

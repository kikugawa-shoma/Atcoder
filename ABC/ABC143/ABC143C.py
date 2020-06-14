N = int(input())
S = input()

count = 0
prev_s = ""

for s in S:
    if prev_s != s:
        count += 1
        prev_s = s

print(count)


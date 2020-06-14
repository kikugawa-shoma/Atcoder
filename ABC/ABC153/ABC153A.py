H, A = map(int, input().split())

num = H//A
w = H % A
if w != 0:
    num += 1
print(num)
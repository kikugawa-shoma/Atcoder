N = int(input())
S = input()
"""
10
ZABCDBABCQ
"""

num = 0
for i in range(len(S)-2):
    if S[i:i+3] == "ABC":
        num += 1

print(num)


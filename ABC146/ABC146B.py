N = int(input())
S = input()


def next_large_char(char, num):
    char_code = ord(char)
    if char_code + num > 90:
        return chr(char_code + num - ord("Z") + ord("A")-1)
    else:
        return chr(char_code + num)


nextS = [0]*len(S)
for i in range(len(S)):
    nextS[i] = next_large_char(S[i], N)

print("".join(nextS))

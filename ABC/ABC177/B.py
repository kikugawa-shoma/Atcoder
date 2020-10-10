s = input()
t = input()

ls = len(s)
lt = len(t)

score = [0]*ls

for i in range(ls-lt+1):
    for j in range(lt):
        if t[j] == s[i+j]:
            score[i] += 1

print(lt-max(score))


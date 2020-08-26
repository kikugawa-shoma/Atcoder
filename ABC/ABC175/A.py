S = input()
pre_weather = "S"

cnt = 0
ans = 0
for i in range(3):
    if pre_weather == "R" and S[i] == "R":
        cnt += 1
    elif S[i] == "R":
        cnt = 1
    pre_weather = S[i]
    
    ans = max(cnt,ans)

print(ans)
    
    

    

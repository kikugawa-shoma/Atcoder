X=int(input())

M=130

for i in range(-130,130):
    for j in range(-130,130):
        if i**5-j**5==X:
            print(i,j)
            break
    else:
        continue
    break

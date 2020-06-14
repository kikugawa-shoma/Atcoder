n = input()
hons = (2,4,5,7,9)
pons = (0,1,6,8)
bons = (3)
if int(n[-1]) in hons:
    print("hon") 
elif int(n[-1]) in pons:
    print("pon")
else:
    print("bon")
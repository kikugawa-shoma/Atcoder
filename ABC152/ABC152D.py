#N = int(input())

N = 100

str_N = str(N)
num = 0
char_set = {str(i) for i in range(1, N)}

for n1 in range(1, min(N, 100)):
    for n2 in range(1, min(N, 100)):
        str_n1, str_n2 = map(str, [n1, n2])
        length1 = len(str_n1)
        length2 = len(str_n2)

        if str_n1[0] == str_n2[length2-1] and str_n1[length1-1] == str_n2[0]:
            if length1 == 1 and length2 == 1:
                num += 1
            if length1 + length2 == 4:
                for k in range(len(str_N)-2):
                    #num = num + 9**k
                for n in range(10**(len(str_N)-2)):
                    if int(str_n1[0]+str(n)+str_n1[length1-1]) <= N:
                        #num += 1
            if length1 == 1 and length2 == 2:
                for k in range(len(str_N)-2):
                    num = num + 9**k
                for n in range(10**(len(str_N)-2)):
                    if int(str_n1[0]+str(n)+str_n1[length1-1]) <= N:
                        num += 1
            if length1 == 2 and length2 == 1:
                for k in range(len(str_N)-2):
                    num = num + 9**k
                for n in range(10**(len(str_N)-2)):
                    if int(str_n1[0]+str(n)+str_n1[length1-1]) <= N:
                        num += 1







print(int(num))




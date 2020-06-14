K = int(input())

lunlun = [1,2,3,4,5,6,7,8,9]
p = 0

def lunlun_generator(now_lunlun):
    last = now_lunlun%10
    if last-1>=0:
        yield 10*now_lunlun+last-1
    yield 10*now_lunlun+last
    if last+1<=9:
        yield 10*now_lunlun+last+1 

while 1:
    for new_lunlun in lunlun_generator(lunlun[p]):
       lunlun.append(new_lunlun)

    p += 1
    if p == K:
        break

print(lunlun[p-1])




from collections import deque
K = int(input())
q = deque([[1],[2],[3],[4],[5],[6],[7],[8],[9]])
cnt = 0
while cnt != K:
    nums = q.popleft()
    last = nums[-1]
    if last == 9:
        tmp = nums.copy()
        tmp.append(8)
        q.append(tmp)

        tmp = nums.copy()
        tmp.append(9)
        q.append(tmp)
    elif last == 0:
        tmp = nums.copy()
        tmp.append(0)
        q.append(tmp)

        tmp = nums.copy()
        tmp.append(1)
        q.append(tmp)
    else:
        tmp = nums.copy()
        tmp.append(last-1)
        q.append(tmp)

        tmp = nums.copy()
        tmp.append(last)
        q.append(tmp)

        tmp = nums.copy()
        tmp.append(last+1)
        q.append(tmp)

    cnt += 1
ans = 0
l = len(nums)
for i in range(l):
    ans += nums[i]*10**(l-i-1)
print(ans)
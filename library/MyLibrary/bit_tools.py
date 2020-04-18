def bit_01(keta):
    ans = []
    for i in range(2**(keta)):
        ans.append("".join(["{:0", str(keta), "b}"]).format(i))
    return ans


print(bit_01(3))

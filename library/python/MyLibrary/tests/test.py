import copy

#pythonでは関数への引数は参照渡し
def mat_change(M):
    M[0][0] = 1

#関数内でcopyすれば値渡しっぽく使える。
def mat_change2(A):
    M = copy.deepcopy(A)
    M[0][0] = 2

A = [[0,0],[0,0]]
print(A," : 元の行列")

mat_change(A)
print(A," : 参照渡しなので変更される")

mat_change2(A)
print(A, " : copyを使えば値渡しっぽく使える")


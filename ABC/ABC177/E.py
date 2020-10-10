import copy
from collections import defaultdict
import math

N = int(input())
A = list(map(int,input().split()))

def fast_prime_factrization(A):
    maxA = max(A)
    D = [-1]*(maxA+1)
    for i in range(2,maxA+1):
        if D[i] != -1:
            continue
        for j in range(1,maxA+1):
            if i*j > maxA:
                break
            if D[i*j] == -1:
                D[i*j] = i
    pr_facts = [defaultdict(int) for i in range(len(A))]
    for i,a in enumerate(A):
        X = a
        while 1:
            if X == D[X]:
                pr_facts[i][D[X]] += 1
                break
            else:
                pr_facts[i][D[X]] += 1
                X //= D[X]
    return pr_facts

def check_sc():
    gcd = A[0]
    for i in range(1,len(A)):
        gcd = math.gcd(gcd,A[i])
    return gcd == 1

def check_pc():
    pr_facts = fast_prime_factrization(A)
    maxA = max(A)
    d = [False]*(maxA+1)
    ret = True
    for i in range(len(pr_facts)):
        for key in pr_facts[i].keys():
            if d[key]:
                ret = False
                break
            d[key] = True
        else:
            continue
        break
    return ret
                
pc = check_pc()
sc = check_sc()

if pc:
    print("pairwise coprime")
elif sc:
    print("setwise coprime")
else:
    print("not coprime")













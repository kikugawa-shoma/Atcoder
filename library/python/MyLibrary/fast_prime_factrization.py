import copy
from collections import defaultdict
import random

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

if __name__ == "__main__":
    A = [random.randint(2,100000) for _ in range(100000)]
    tmp = fast_prime_factrization(A)

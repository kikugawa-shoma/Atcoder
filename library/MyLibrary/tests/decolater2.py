#キャッシュ有とキャッシュ無でのフィボナッチ数列の計算時間の比較
import time
from functools import lru_cache


def main1():
    def fib(n):
        if n < 2:
            return n
        else:
            return fib(n - 1) + fib(n - 2)

    for i in range(30):
        fib(i)

def main2():
    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        else:
            return fib(n - 1) + fib(n - 2)

    for i in range(100):
        fib(i)

if __name__ == "__main__":
    start = time.time()
    main1()
    print(time.time() - start)

    start = time.time()
    main2()
    print(time.time() - start)


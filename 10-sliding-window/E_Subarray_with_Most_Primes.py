# ================================
# Author: Pritam
# ================================


import sys
input = sys.stdin.readline
# ---------- Helpers ----------
def ceil(a, b):    ##relation b/w floor division and ceil division
    return (a+b-1)//b
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def ins():
    return input().strip()
def inmap():
    return map(int, input().split())
def print_fast(*args):
    sys.stdout.write(" ".join(map(str, args)) + '\n')
# ---------- Solve Function ----------
def countFactors(x):
    cnt = 0
    for d in range(1, int(x**0.5)+1):
        if x%d == 0:
            if x//d == d:
                cnt += 1
            else:
                cnt += 2
    return cnt


def isPrime(x):
    if countFactors(x) == 2:
        return True
    return False

def main():
    n, k = inmap()
    a = inlt()
    cnt = 0
    for i in range(k):
        if isPrime(a[i]):
            cnt += 1

    maxCnt = cnt
    l, r = 0, k-1

    for i in range(k, n):
        if isPrime(a[i]):
            cnt += 1
        if isPrime(a[i-k]):
            cnt -= 1

        ## the window is i-k+1, i
        if cnt > maxCnt:
            maxCnt = cnt
            l, r = i-k+1, i
    print_fast(*a[l:r+1])    


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
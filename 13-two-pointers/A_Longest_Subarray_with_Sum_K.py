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







def main():
    n, k = inmap()
    a = inlt()
    ans, l, curSum = 0, 0, 0
    for r in range(n):
        curSum += a[r]
        while curSum >= k:
            curSum -= a[l]
            l += 1
        ans = max(ans, r-l+1)
    print(ans)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
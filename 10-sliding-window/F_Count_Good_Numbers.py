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
    n, m, k = inmap()
    arr = inlt()
    good = inlt()

    good = set(good)
    ans = []
    cnt = 0
    for i in range(k):
        if arr[i] in good:
            cnt += 1
    ans.append(cnt)

    for i in range(k, n):
        if arr[i] in good:
            cnt += 1
        if arr[i-k] in good:
            cnt -= 1
        ans.append(cnt)
    print_fast(*ans)

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
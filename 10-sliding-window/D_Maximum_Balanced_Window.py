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
    arr = inlt()

    cnt = 0
    maxCnt = 0
    window = sum(arr[:k])
    cnt += window
    if window < k:
        cnt += 1
    maxCnt = max(maxCnt, cnt)
    for i in range(k, n):
        window += arr[i]
        window -= arr[i-k]
        cnt = window
        if window <k:
            cnt += 1
        maxCnt = max(maxCnt, cnt)

    print_fast(maxCnt)

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
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
    n, k, t = inmap()
    arr = inlt()
    sum_of_window = sum(arr[:k])
    cnt = 0
    if sum_of_window>=t*k:
        cnt += 1
    for i in range(k, n):
        sum_of_window += arr[i]
        sum_of_window -= arr[i-k]
        if sum_of_window >= t*k:
            cnt += 1
    print_fast(cnt)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
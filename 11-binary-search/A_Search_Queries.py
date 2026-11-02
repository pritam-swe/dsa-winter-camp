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
    n, q = inmap()
    a = inlt()
    def bs(x):
        l, r = 0, n-1
        while l<=r:
            mid = l+((r-l)//2)
            if a[mid] == x:
                return mid+1
            elif a[mid] > x:
                r = mid -1
            else:
                l = mid + 1
        return -1
    ans = []
    for _ in range(q): 
        x = inp()
        print_fast(bs(x))



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
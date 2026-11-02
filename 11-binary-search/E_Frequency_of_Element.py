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

FIRST = 1
LAST = 2

def getOcc(a, x, config):
    l, r = 0, len(a)-1
    ans = -1
    while l<=r:
        mid = l + (r-l)//2
        if a[mid] == x:
            ans = mid
            if config == FIRST:
                r = mid -1
            else:
                l = mid + 1
        elif a[mid] > x:
            r = mid -1
        else:
            l = mid+1
    return ans

def main():
    n, q = inmap()
    a = inlt()
    a.sort()
    for _ in range(q):
        x = inp()
        f = getOcc(a, x, FIRST)
        if f == -1:
            print(0)
            continue
        l = getOcc(a, x, LAST)
        print(l-f+1)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
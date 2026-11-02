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
'''
def firstOccurrence(a, x):
        n = len(a)
        l, r = 0, n-1
        ans = -1
        while l<=r:
            mid = l+((r-l)//2)
            if a[mid] == x:
                ans = mid
                r = mid -1
            elif a[mid] > x:
                r = mid -1
            else:
                l = mid+1
        return ans

def lastOccurrence(a, x):
        n = len(a)
        l, r = 0, n-1
        ans = -1
        while l<=r:
            mid = l+((r-l)//2)
            if a[mid] == x:
                ans = mid
                l = mid +1
            elif a[mid] > x:
                r = mid -1
            else:
                l = mid+1
        return ans


'''



FIRST_OCC = 1
LAST_OCC = 2
def getOcc(a, x, config):
    n = len(a)
    l, r = 0, n-1
    ans = -1
    while l<=r:
        mid = l+((r-l)//2)
        if a[mid] == x:
            ans = mid
            if config == FIRST_OCC:
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
    
    for _ in range(q):
        x = inp()

        first = getOcc(a, x, FIRST_OCC)
        if first == -1:
            print(-1)
            continue
        last = getOcc(a, x, LAST_OCC)

        print(f"{first+1} {last + 1}")


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
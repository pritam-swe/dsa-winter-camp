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
    n = inp()
    names = []
    for _ in range(n):
        s = ins()
        names.append(s)
    target = ins()

    low, high = 0, n-1
    while low <= high:
        mid = low + (high - low)//2
        if names[mid] == target:
            print("YES")
            return
        elif names[mid] > target:
            high = mid-1

        else:
            low = mid+1
    print("NO")
    return
 

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
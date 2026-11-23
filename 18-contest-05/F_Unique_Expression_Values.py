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


def bt(n, arr, idx, cal, ans):
    if idx == n:
        ans.add(cal)
        return

    bt(n, arr, idx+1, cal+arr[idx], ans)
    
    bt(n, arr, idx+1, cal-arr[idx], ans)


## arr[0] is always positive


def main():
    n = inp()
    arr = inlt()
    ans = set()
    bt(n, arr, 1, cal=arr[0], ans=ans)
    print(len(ans))

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
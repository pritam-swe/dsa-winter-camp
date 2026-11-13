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
    freq = dict()
    l, ans = 0, 0
    for r in range(n):
        freq[a[r]] = freq.get(a[r], 0) + 1
        while len(freq) > k:
            freq[a[l]] -= 1
            if freq[a[l]] == 0:
                del freq[a[l]]
            l+=1
        ans += r-l+1
    print(ans)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
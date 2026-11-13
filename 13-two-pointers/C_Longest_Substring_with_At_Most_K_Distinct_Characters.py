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
    s = ins()
    l, ans = 0, 0
    freq = dict()

    for r in range(n):
        freq[s[r]] = freq.get(s[r], 0) + 1
        while len(freq) > k:
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l += 1
        ans = max(ans, r-l+1)
    print(ans)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
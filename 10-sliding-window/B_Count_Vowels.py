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

vowel = {"a", 'e', 'i', 'o', 'u'}

def main():
    n, k = inmap()
    s = ins().lower()
    ans = []
    cnt = 0
    for i in range(k):
        if s[i] in vowel:
            cnt += 1
    ans.append(cnt)

    for i in range(k, n):
        if s[i] in vowel:
            cnt += 1
        if s[i-k] in vowel:
            cnt -= 1
        ans.append(cnt)

    print_fast(*ans)

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
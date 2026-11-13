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
    s = ins()
    l, ans = 0, 0
    st = set()
    for r in range(n):
        while s[r] in st:
            st.remove(s[l])
            l+=1
        
        st.add(s[r])
        ans = max(ans, r-l+1)
    print(ans)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
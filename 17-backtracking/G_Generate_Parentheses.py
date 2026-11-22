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

def bt(n, open, close, path, ans):
    
    if open == n and close == n:
        ans.append(path.copy())
        return

    if open<n:
        path.append('(')
        bt(n, open+1, close, path, ans)
        path.pop()

    if close < open:
        path.append(')')
        bt(n, open, close+1, path, ans)
        path.pop()






def main():
    n = inp()
    ans = []
    bt(n, 0, 0, [], ans = ans)
    print(len(ans))
    for paths in ans:
        print_fast(''.join(paths))

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
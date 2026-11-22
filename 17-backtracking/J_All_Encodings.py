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


def bt(s, idx, path, ans):
    if idx == len(s):
        ans.append(path[:])
        return
        
    if s[idx] == 0:
        return
    ## take 1 digit
    d1 = int(s[idx])
    if 1 <= d1 <=9:
        path.append(chr(d1+96))
        bt(s, idx+1, path, ans)
        path.pop()
    ## take 2 digit
    if idx+1 < len(s):
        d2 = int(s[idx] + s[idx+1])
        if 10<= d2 <=26:
            path.append(chr(d2+96))
            bt(s, idx+2, path, ans)
            path.pop()


def main():
    s = ins()
    ans = []
    bt(s, idx=0, path=[], ans=ans)
    print(len(ans))
    for paths in ans:
        print_fast(''.join(paths))

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
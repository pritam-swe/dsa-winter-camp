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



def backtrack(n, curr, path):
    if curr == n:
        print(*path)
        return
    if curr > n:
        return

    ## 1 jump
    path.append(1)
    backtrack(n, curr + 1, path)
    path.pop()

    ## two jump
    path.append(2)
    backtrack(n, curr+2, path)
    path.pop()

def main():
    n = inp()
    backtrack(n, 0, [])



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
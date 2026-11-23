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


def bt(n,m, mat, x, y, path):
    if x == n-1 and y == m-1:
        print_fast(''.join(path))
        return
    if x >=n or y >= m:
        return
    if mat[x][y] == 1:
        return

    path.append('R')
    bt(n, m, mat, x, y+1, path)
    path.pop()

    path.append('D')
    bt(n, m, mat, x+1, y, path)
    path.pop()




def main():
    n,m = inmap()
    mat = [inlt() for _ in range(n)]
    bt(n, m, mat, 0, 0, [])

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
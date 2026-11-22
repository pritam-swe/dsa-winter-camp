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



def backtrack(n, m, curr_row, curr_col, path):
    if curr_col == m and curr_row == n:
        print(''.join(path))
        return
    if curr_col > m or curr_row > n:
        return
    path.append("R")
    backtrack(n, m, curr_row, curr_col+1, path)
    path.pop()
    
    path.append("D")
    backtrack(n, m, curr_row+1, curr_col, path)
    path.pop()



def main():
    n, m = inmap()
    backtrack(n, m, 1, 1, [])


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
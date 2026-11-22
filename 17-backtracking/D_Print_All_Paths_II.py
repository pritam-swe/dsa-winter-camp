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



def backtrack(n, m, x, y, path, mat:list[list]):
    '''
    x: row
    y: col
    '''
    if y == m-1 and x == n-1:
        print(''.join(path))
        return
    if y >= m or x >= n:
        return
    if mat[x][y] == 1:
        return
    path.append("R")
    backtrack(n, m, x, y+1, path, mat)
    path.pop()
    
    path.append("D")
    backtrack(n, m, x+1, y, path, mat)
    path.pop()




def main():
    n, m = inmap()
    mat= [inlt() for _ in range(n)]
    backtrack(n, m, 0, 0, [], mat)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
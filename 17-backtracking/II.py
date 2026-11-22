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



def backtrack(n, curr, path, k):
    if curr == n:
        print(*path)
        return
    if curr > n:
        return

    for jump in range(1, k+1):
        path.append(jump)
        backtrack(n, curr + jump, path, k)
        path.pop()


def main():
    n, k = inmap()
    backtrack(n, 0, [], k = k)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
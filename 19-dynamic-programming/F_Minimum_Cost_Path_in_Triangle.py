# ================================
# Author: Pritam
# ================================


import sys
input = sys.stdin.readline
INT_MAX = float('inf')
INT_MIN = float('-inf')
MOD = 10**9 + 7
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

from types import GeneratorType
## custom stack manager for python to avoid RTE in cf using python
def bootstrap(f, stack=None):
    if stack is None: stack = []
    def func_wrapper(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to
    return func_wrapper

@bootstrap
def f(x, y, dest, dp, cost):
    if x == dest-1:
        yield cost[x][y]

    if dp[x][y] != -1:
        yield dp[x][y]
    ans1 = yield f(x+1, y, dest, dp, cost)
    ans2 = yield f(x+1, y+1, dest, dp, cost)

    dp[x][y] = cost[x][y] + min(ans1, ans2)
    yield dp[x][y]



def main():
    n = inp()
    triangle = [inlt() for _ in range(n)]
    dp = [[-1]*i for i in range(1, n+1)]
    ans = f(0, 0, n, dp, triangle)
    print(ans)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
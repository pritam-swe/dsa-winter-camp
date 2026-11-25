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
def f(n, cost, pos, dp):
    if pos > n:
        yield INT_MAX
    if pos == n:
        yield 0
    if dp[pos] != -1:
        yield dp[pos]

    smallAns1 = yield f(n, cost, pos+1, dp)
    smallAns2 = yield f(n, cost, pos+2, dp)

    dp[pos] = cost[pos] + min(smallAns2,smallAns1)
    yield dp[pos]
    yield


def main():
    n = inp()
    cost = [0]+inlt()
    if n == 1:
        print(cost[1])
        return
    dp = [-1]*(n+1)
    ans = f(n+1, cost, 0, dp)
    print(ans)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
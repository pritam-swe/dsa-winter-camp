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
def fo(n, arr, target):
    if n == 0:
        yield -1
    smallAns = yield fo(n-1, arr, target)
    if smallAns != -1:
        yield (smallAns)
    if arr[n-1] == target:
        yield n
    yield -1

# def fo(n, arr, x):
#     if n==0:
#         return -1
#     smallAns = fo(n-1, arr, x)
#     if smallAns != -1:
#         return smallAns
#     if arr[n-1] == x:
#         return n
#     return -1


def main():
    n = inp()
    arr = inlt()
    x = inp()
    print(fo(n, arr, x))


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
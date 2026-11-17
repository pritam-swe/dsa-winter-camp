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
def toh(n: int, src: str, aux: str, dest: str):
    if n==0: yield
    yield toh(n-1, src, dest, aux)
    print(f"Move {src} to {dest}")
    yield toh(n-1, aux, src, dest)
    yield

# move top n-1 disk: from Src to Aux
# move the largest disk: from Src to Dest
# move the rest n-1 disk: from Aux to Dest


def main():
    n = inp()
    toh(n, "A", "B", "C")


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    for _ in range(t):
    # t = inp()
        main() 
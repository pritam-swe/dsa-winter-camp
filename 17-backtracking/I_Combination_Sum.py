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


def bt(n, x, arr, idx, path, ans, s):
    if s==x:
        ans.append(path[:])
        return
    if idx == n or s>x:
        return

    path.append(arr[idx])
    bt(n, x, arr, idx, path, ans, s+arr[idx])   ##take same multiple times
    path.pop()

    bt(n, x, arr, idx+1, path, ans, s)




def main():
    n, x = inmap()
    a = inlt()
    ans = []
    bt(n, x, arr = a, idx=0, path=[], ans = ans, s=0)
    print(len(ans))
    for paths in ans:
        print_fast(len(paths), *paths)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
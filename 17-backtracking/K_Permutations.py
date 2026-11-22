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

def bt(n, arr, idx, ans):
    if idx == n:
        ans.append(arr[:])
        return

    ## observe: we just have to keep swapping the array
    for i in range(idx, n):
        arr[idx], arr[i] = arr[i], arr[idx]
        bt(n, arr, idx+1, ans)
        arr[idx], arr[i] = arr[i], arr[idx]







def main():
    n = inp()
    arr = inlt()
    ans = []
    bt(n, arr, 0, ans=ans)
    print(len(ans))
    for perms in ans:
        print_fast(*perms)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
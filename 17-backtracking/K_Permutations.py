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

def bt(n, arr, idx, ans, path):
    if idx == n:
        ans.append(path[:])
        return

    ## observe: we just have to keep swapping the array
    # for i in range(idx, n):
    #     arr[idx], arr[i] = arr[i], arr[idx]
    #     bt(n, arr, idx+1, ans)
    #     arr[idx], arr[i] = arr[i], arr[idx]

    ## the second though process:
    ## think in terms of placing the elements
    ## placement approach
    for i in range(n):
        if path[i] == None:
            path[i] = arr[idx]
            bt(n, arr, idx+1, ans, path)
            path[i] = None
    

  



def main():
    n = inp()
    arr = inlt()
    ans = []
    path = [None]*n
    bt(n, arr, 0, ans=ans, path=path)
    print(len(ans))
    for perms in ans:
        print_fast(*perms)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
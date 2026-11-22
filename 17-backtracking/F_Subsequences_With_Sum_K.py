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

def bt(n, arr, k, idx, path, ans, sum, cnt):
    if idx == n:
        if sum == k:
            cnt[0] += 1
            ans.append(path.copy())
            return
        return

    path.append(arr[idx])
    bt(n, arr, k, idx+1, path, ans, sum+arr[idx], cnt)
    path.pop()

    bt(n, arr, k, idx+1, path, ans, sum, cnt)








def main():
    n, k = inmap()
    a = inlt()
    ans = []
    cnt = [0] ##new concept learnt, how to count inside a function from a parameter. list is mutable int is not
    bt(n, a, k, 0, [], ans=ans, sum =0, cnt=cnt)
    # print(len(ans))
    print(*cnt)
    for paths in ans:
        print_fast(*paths)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
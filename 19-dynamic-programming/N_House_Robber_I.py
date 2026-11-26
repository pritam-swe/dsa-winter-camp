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

sys.setrecursionlimit(10**6)    ## submit in python 3 -> python3 is slower but has a higher stack
def max_amount(n, arr, idx, dp):

    if idx >= n:
        return 0

    # i can either rob or skip
    if dp[idx] != -1:
        return dp[idx]
    #rob
    ans1 = arr[idx] + max_amount(n, arr, idx+2, dp) #we have to skip the adjacent

    #skip
    ans2 = 0 + max_amount(n, arr, idx+1, dp)
    dp[idx] = max(ans1, ans2)
    return dp[idx]



def main():
    n = inp()
    house = inlt()
    dp = [-1 for _ in range(n)]
    print_fast(max_amount(n, house, 0, dp))


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
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







def main():
    n, k = inmap()
    nums = inlt()
    map = dict()
    for i in range(k):
        map[nums[i]] = map.get(nums[i], 0) + 1
    ans = []
    ans.append(len(map))
    for i in range(k, n):
        map[nums[i]] = map.get(nums[i], 0) + 1
        map[nums[i-k]] -= 1
        if map[nums[i-k]] == 0:
            del map[nums[i-k]]
        ans.append(len(map))
    print_fast(*ans)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
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

dice = [x for x in range(1,7)]

def bt(k, s, path):
    if s == k:
        print_fast(*path)
        return
    
    if s > k:
        return

    
    ## take 1 num multiple times
    for roll_val in range(1, 7):
        path.append(roll_val)
        bt(k, s+roll_val, path)
        path.pop()

    # bt(idx+1, k, s, path)



def main():
    k = inp()
    bt(k, 0, [])

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
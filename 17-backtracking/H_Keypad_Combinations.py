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

keymap = {
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz'
}

def bt(s, idx, path, ans):
    if idx == len(s):
        ans.append(path[:])
        return

    digit = s[idx]
    chars = keymap[digit]

    for ch in chars:
        path.append(ch)
        bt(s, idx+1, path, ans)
        path.pop()



def main():
    s = ins()
    ans = []
    bt(s, 0, [], ans=ans)
    print_fast(len(ans))

    for paths in ans:
        print_fast(''.join(paths))


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 
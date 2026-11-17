def fo(A, n, target):
    smallAns = fo(A, n-1, target)
    if smallAns != -1:
        return smallAns
    if A[n-1] == target:
        return n-1
    return -1

arr = [1, 7, 7, 7, 7, 5, 8, 9]
n = len(arr)
print(fo(arr, n, 7))
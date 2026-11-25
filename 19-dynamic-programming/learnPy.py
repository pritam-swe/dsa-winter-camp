n, m = 2, 3
l1 = [[-1]*n]*m

print("l1")
print("------------")
print(l1)
l1[0][0] = 100
print(l1)

l2 = [[-1]*m for _ in range(n)]
print("\nl2")
print("------------")
print(l2)
l2[0][0] = 100
print(l2)
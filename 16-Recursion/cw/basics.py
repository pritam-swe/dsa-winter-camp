# # ## print 1 to n
# # def fn(n):
# #     if n == 0:
# #         return
# #     fn(n-1)
# #     print(n, end=" ")

# # fn(5)


# # ## print n to 1
# # def fn(n):
# #     if n == 0:
# #         return
# #     fn(n-1)
# #     print(n, end=" ")

# # fn(5)


# ## print zig zag
# def fn(n):
#     if n == 1:
#         return
#     print(n, end=" ")
#     fn(n-1)

# fn(5)
# def fn(n):
#     if n == 0:
#         return
#     fn(n-1)
#     print(n, end=" ")

# fn(5)


# zig zag with 1 fn
def fn(n):
    if n==1:
        print(1)
        return
    print(n)
    fn(n-1)
    print(n)

fn(3)



### print numbers in reverse
# n = 1950 -> 0591
# n = 1234 -> 4321

# def printRev(n: int):
#     if n == 0:
#         return
#     print(n%10, end="")
#     printRev(n//10)


# def fact(n):
#     if n<= 1:
#         return n

# def sumN(n):
#     if n == 0:
#         return 0
#     smallAns = sumN(n-1)
#     ans = smallAns + n
#     return ans
# print(sumN(5))

fn(3)
    
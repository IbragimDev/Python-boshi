# import random as r

# from math import sqrt

# print(math.pow(6, 3))

# kv = lambda x, y: x**y
# print(kv(6, 3))


# def result(n):
#     return lambda x: x**n


# kv = result(3)
# print(kv(6))
# kub = result(10)
# print(kub(10))

# numbers = list(range(11))
# ildizs = list(map(sqrt, numbers))
# print(ildizs)

# def kv(x):
#     return x**x
# print(list(map(kv, numbers)))
# kv = list(map(lambda x: x * x, numbers))
# print(kv)

# a = [4, 6, 8]
# b = [10, 12, 14]
# a_and_b = list(map(lambda x, y: x + y, a, b))
# print(a_and_b)


# nums = r.sample(range(0, 100), 10)
# print(nums)
# def nums2(x):
#     return x % 2 == 0
# print(nums2(6))

# infos = list(filter(lambda num: num % 2 == 0, nums))
# print(infos)

mevalar = ["olma", "nok", "beho", "anjir", "uzum", "kiwi", "banan", "gilos"]
# harf = "b"
# mevas = list(filter(lambda meva: meva.startswith(harf), mevalar))
# print(mevas)

# mevalar2 = list(filter(lambda meva: len(meva) < 5, mevalar))
# print(mevalar2)

meva2 = list(
    filter(lambda meva: (meva.startswith("a") and meva.endswith("r")), mevalar)
)
print(meva2)

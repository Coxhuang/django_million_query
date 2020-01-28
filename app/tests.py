from django.test import TestCase

# for foo in range(1,30001):
#     i = (foo+2) // 3
#     print(foo,i)

# import random
#
# a = random.randint(1,10)
# print(a)

#
# for foo in range(1,30001):
#     for j in range(1,4):
#         print(foo,3*(foo-1)+j)


import copy

a = ["1","2",["1","3"]]
print(id(a))
b = copy.deepcopy(a)
print(id(b))
b[2][0] = "88"
print(a,"---",b)


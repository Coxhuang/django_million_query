from django.test import TestCase

# for foo in range(1,30001):
#     i = (foo+2) // 3
#     print(foo,i)

# import random
#
# a = random.randint(1,10)
# print(a)


for foo in range(1,30001):
    for j in range(1,4):
        print(foo,3*(foo-1)+j)

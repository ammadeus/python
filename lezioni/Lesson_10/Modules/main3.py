import mypackage

res1 = mypackage.module1.sum_three_numbers(1, 2, 3)
res2 = mypackage.module2.sum_two_numbers(1, 2)
print(res1, res2)

# ---------------------------------------

# import mypackage.module1
# import mypackage.module2

# res = mypackage.module1.sum_three_numbers(1, 2, 3)
# print(res)

# res2 = mypackage.module2.sum_two_numbers(1, 2)  # how to fix this?
# print(res2)

# ---------------------------------------

# from mypackage import module1 as m1, module2 as m2

# res = m1.sum_three_numbers(1, 2, 3)
# print(res)

# ---------------------------------------

# subpackages

# import mypackage.subpackage.module3

# print(mypackage.subpackage.module3.multiply(2, 3))

# ---------------------------------------

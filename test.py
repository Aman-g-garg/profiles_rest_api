# # # print([x for x in range(1,5) if  x % 2 == 0])

# # test_dict = {
# #     'a': 'A',
# #     'b': 'B',
# #     'c': 'C',
# #     'd': 'D',
# # }

# # print({key:value for key, value in test_dict.items() if  value != 'A'})

# import copy

# # list_1 = [[1,3],[4,6], [7,9]]
# # new_list = copy.copy(list_1)
# # new_list.append(["1","3"])
# # new_list[0][1] = [8, "9"]
# # print("Original List:\n", list_1)
# # print("\nNewly Created List (Copy):\n", new_list)

# # Modifying the original list will not affect the copied list and vice versa

# def test(fun):
#     def inner():
#         print("Running Test")
#         fun()
#         print("Test Passed!")
#     return inner

# def fun_test():
#     print("fun_test function")

# x = test(fun_test)
# x()
    
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# print(list(map(lambda x, y: x+y, l1, l2)))

# l1 = [22,55,43,63,12,32]

# def test(nums):
#     if nums < 34:
#         return False
#     else:
#         return True
    
# for i in filter(test, l1):
#     print(i)

import pandas as pd





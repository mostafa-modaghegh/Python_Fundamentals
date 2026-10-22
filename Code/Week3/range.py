#range(start=0,stop,step=1)
nums = range(10,20,2)
print(nums)
print(list(nums))



#100   105  110 ...      995
nums = range(100,1000,5)
nums_list = list(nums)
print(nums_list)


if 238 in nums_list:
    print("238 is in nums list")
else:
    print("238 is not in nums list")

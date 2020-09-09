# a = 10
# b = 20
list = (1, 2, 3, 4, 5)
123
# if (a in list):
#     print "1 - 变量 a 在给定的列表中 list 中"
# else:
#     print "1 - 变量 a 不在给定的列表中 list 中"

# if (b notde in list):
#     print "2 - 变量 b 不在给定的列表中 list 中"
# else:
#     print "2 - 变量 b 在给定的列表中 list 中"

# # 修改变量 a 的值
# a = 2
# if (a in list):
#     print("3 - 变量 a 在给定的列表中 list 中")
# else:
#     print("3 - 变量 a 不在给定的列表中 list 中")


# def isLeapYear(year):
#     #  if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     #      print(year)
#     #      return True
#     return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


# a = isLeapYear(2019)
# print(a)
# return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
def findDuplicates(self, nums: List[int]) -> List[int]:
   if len(nums) <= 1:
        return nums
    for i in range(len(nums)):
        if(nums[i] < 0 or nums[i] > len(nums)-1):
            return nums
    for i in range(len(nums)):
        while(nums[i] != i):
            if(nums[nums[i]] == nums[i]):
                nums.append(nums[i])
                break
        temp = nums[i]
        nums[i] = nums[temp]
        nums[temp] = temp
    return nums

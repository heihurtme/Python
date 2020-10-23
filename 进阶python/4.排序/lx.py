from typing import List
from suiji import suiji

# List1 = suiji.suiji(11)
# def buddling(List1:List[int]) -> List:
#     if len(List1) <= 1:
#         return List1
#     for i in range(1,len(List1)):
#         for j in range(len(List1) - i):
#             if List1[j] > List1[j + 1]:
#                 List1[j],List1[j + 1] = List1[j + 1],List1[j]
#     return List1
# if __name__ == '__main__':
#     print(buddling(List1))
#
# def choice(List2:List[int]) -> List:
#     for i in range(len(List2)-1):
#         min_index = i
#         for j in range(i+1,len(List2)):
#             if List2[j] < List2[min_index]:
#                 min_index = j
#         if min_index != i:
#             List2[min_index],List2[i] = List2[i],List2[min_index]
#     return List2
# if __name__ == '__main__':
#     List2 = suiji.suiji(10)
#     print(choice(List2))

def insertSort(nums:List[int]) -> List:
    if len(nums) < 2:
        return nums
    for right in range(1,len(nums)):
        target = nums[right]
        for left in range(right):
            if nums[left] > target:
                nums[left+1:right+1] = nums[left:right]
                nums[left] = target
                break
        print("第{}轮：".format(right),end ="\n")
        print(nums)
    return nums

if __name__ == '__main__':
    nums=suiji.suiji(10)
    print(insertSort(nums))

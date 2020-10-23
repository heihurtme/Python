from typing import List
from suiji import suiji

# list1 = [3,96,56,8,52,63,42,51,20,37,48]
# for i in range(1,len(list1)):
#     for j in range(len(list1)-i):
#         if list1[j] > list1[j+1]:
#             list1[j],list1[j+1] = list1[j+1],list1[j]
#     print("第{}轮:".format(i),end="")
#     print(list1)
# print(list1)

def paixu(List1:List[int]) -> List:
    if len(List1) <= 1:
        return List1
    for i in range(1,len(List1)):
        for j in range(len(List1) - i):
            if List1[j] > List1[j + 1]:
                List1[j], List1[j + 1] = List1[j + 1], List1[j]
        print("第{}轮:".format(i),end="")
        print(List1)
    return List1

if __name__ == '__main__':
    List1 = suiji.suiji(11)
    print(paixu(List1))

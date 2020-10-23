# from typing import List
# def fen(List1:List) -> List:
#     a,b = 0,len(List1) - 1
#     i = 0
#     while i <= len(List1) - 1:
#         if List1[i] == 0:
#             List1[i],List1[a] = List1[a],List1[i]
#             i += 1
#             a += 1
#         elif List1[i] == 2:
#             List1[i],List1[b] = List1[b],List1[i]
#             i += 1
#             b -= 1
#         else:
#             i += 1
#     return List1
#
# print(fen([0,2,2,1,0,1,1]))

from typing import List
from suiji import suiji
def maopao(List1:List) -> List:
    for i in range(1,len(List1)):
        for j in range(len(List1)-i):
            if List1[j] > List1[j+1]:
                List1[j],List1[j+1] = List1[j+1],List1[j]
    return List1
a1 = suiji.suiji(10)
print(maopao(a1))


def xuanze(List2:List) -> List:
    for a in range(len(List2)-1):
        min_index = a
        for b in range(a + 1,len(List2)):
            if List2[b] < List2[min_index]:
                min_index = b
        if a != min_index:
            List2[min_index],List2[a] = List2[min_index],List2[a]
    return List2
a2 = suiji.suiji(10)
print(xuanze(a2))

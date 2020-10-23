from typing import List
from suiji import suiji
def insertSort(iList:List) -> List:
    if len(iList) < 2:
        return iList
    for right in range(1,len(iList)):
        target = iList[right]
        for left in range(right):
            if iList[left] > target:
                iList[left + 1:right + 1] = iList[left:right]
                iList[left] = target
                break
        print("第{}轮：".format(right),end="")
        print(iList)
    return iList

if __name__ == '__main__':
    iList = suiji.suiji(10)
    print(insertSort(iList))
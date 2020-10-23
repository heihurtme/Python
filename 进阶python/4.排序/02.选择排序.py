from suiji import suiji
from typing import List

def xuanze(List1:List[int])-> List:
    if len(List1) <= 1:
        return List1
    for i in range(len(List1)-1):
        mindex = i
        for j in range(i+1,len(List1)):
            if List1[j] < List1[mindex]:
                mindex = j
        if i != mindex:
            List1[i],List1[mindex] = List1[mindex],List1[i]
    return List1

if __name__ == '__main__':
    List1 = suiji.suiji(11)
    print(xuanze(List1))



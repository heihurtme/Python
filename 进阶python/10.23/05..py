# def quickSort(nums,start,end):
#     if start >= end:
#         return
#     mid = partition(nums,start,end)
#     quickSort(nums,start,mid - 1)
#     quickSort(nums,mid + 1,end)
#     return nums
#
# def partition(nums,start,end):
#     p = start + 1
#     q = end
#     pivot = nums[start]
#     while p <= q:
#         while p <= q and nums[p] < pivot:
#             p += 1
#         while p <= q and nums[q] >= pivot:
#             q -= 1
#         if p < q:
#             swap(nums,p,q)
#     swap(nums,start,q)
#     return q
#
# def swap(nums,a,b):
#     nums[a],nums[b] = nums[b],nums[a]
#
# if __name__ == '__main__':
#     nums = [9,3,6,5,4,8,2,3,10]
#     print(quickSort(nums,0,len(nums)-1))


# def quickSort(nums):
#     if len(nums) <= 1:
#         return nums
#     else:
#         pivot = nums[0]
#         return quickSort([i for i in nums[1:] if i < pivot]) + \
#             [pivot] + \
#             quickSort([i for i in nums[1:] if i >= pivot])
#
# if __name__ == '__main__':
#     nums = [5,3,6,9,7,1,0,8]
#     print(quickSort(nums))

def quickSort(nums,start,end):
    if start >= end:
        return
    mid = partition(nums,start,end)
    quickSort(nums,start,mid - 1)
    quickSort(nums,mid + 1,end)
    return nums

def partition(nums,start,end):
    slow = start
    pivot = nums[start]
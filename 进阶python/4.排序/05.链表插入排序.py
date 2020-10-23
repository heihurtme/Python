def ListNode():
    pass

def insertSortList(head:ListNode) -> ListNode:
    dummy = ListNode(0)
    pre = dummy

    cur = head
    while cur is not None:
        temp = cur.next
        while pre.next is not None and pre.next.data < cur.data:
            pre = pre.next
        cur.next = pre.next
        pre.next = cur
        cur = temp
        pre = dummy
    return dummy.next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pre = dummy
        cur = head
        while cur:
            tmp = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre= dummy
            cur = tmp
        return dummy.next
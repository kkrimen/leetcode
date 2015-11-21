# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        carry = 0
        res = head
        while l1 or l2:
            curNum = 0
            if l1:
                curNum += l1.val
                l1 = l1.next
            if l2:
                curNum += l2.val
                l2 = l2.next
            curNum += carry
            res.val = curNum % 10
            carry = curNum / 10
            if l1 or l2 or carry:
                res.next = ListNode(None)
                res = res.next
                res.val = carry
        return head

"""
test
"""
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
while result:
    print result.val
    result = result.next
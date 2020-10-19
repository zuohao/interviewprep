# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1: return head
        
        ret = tail = ListNode(-1, None) # dummy head
        while head:
            curr_stack = []
            less_than_k = False
            for i in range(k):
                if head is None:
                    less_than_k = True
                    break
                curr_stack.append(head)
                head = head.next
            
            if less_than_k: # process as a queue
                for node in curr_stack:
                    tail.next = node
                    tail = tail.next
            else: # process as a stack
                for node in curr_stack[::-1]:
                    tail.next = node
                    tail = tail.next
            tail.next = None
        
        return ret.next
    

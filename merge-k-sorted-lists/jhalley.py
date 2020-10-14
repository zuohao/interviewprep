# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [(list.val, list) for list in lists if list is not None]
        heapq.heapify(heap)
        
        ret = lastNode = None 
        while len(heap) > 0:
            item = heapq.heappop(heap)
            if ret == None:
                lastNode = ListNode(item[0], None)
                ret = lastNode
            else:
                lastNode.next = ListNode(item[0], None)
                lastNode = lastNode.next
                
            if item[1].next is not None:
                heapq.heappush(heap, (item[1].next.val, item[1].next))
        
        return ret 

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
        # Initialize to list of current pointers to each linked list
        curPtrs = [l for l in lists if l is not None]
        ret = cur = None
        heap = [(node.val, idx) for idx, node in enumerate(curPtrs)]
        heapify(heap)
        while len(heap) > 0:
            (_, idx) = heappop(heap)
            if ret == None:
                ret = curPtrs[idx]
            else:
                cur.next = curPtrs[idx]
            cur = curPtrs[idx]
            if curPtrs[idx].next != None:
                curPtrs[idx] = curPtrs[idx].next
                heappush(heap, (curPtrs[idx].val, idx))
        return ret
            

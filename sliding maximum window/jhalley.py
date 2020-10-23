class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h = [(-nums[i], i) for i in range(k)]
        heapq.heapify(h) # maxheap first K elements
        ret = [-h[0][0]] 
        
        for i in range(k, len(nums)):
            h.append((-nums[i], i))
            heapq.heapify(h)
            
            while True:
                root = heapq.heappop(h)
                if root[1] > i-k:
                    break
                
            ret.append(-root[0])
            h.append(root)
        
        return ret

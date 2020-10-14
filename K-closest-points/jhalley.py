# First attempt
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # calculate euc dist of all points
        # put in heap
        # return first K
        
        h = []
        for point in points:
            heapq.heappush(h, (self.calcDist(point), point))
        return  [heapq.heappop(h)[1] for i in range(K)]
    
    def calcDist(self, p):
        return (p[0]**2+p[1]**2)**0.5

# Multiple attempts later
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # create a maxheap of size up to K
        
        calcDist = lambda p: -(p[0]**2+p[1]**2)
        h=[]
        
        for point in points:
            heapq.heappush(h, (calcDist(point), point))
            if len(h) > K:
                heapq.heappop(h)
                
        return [i[1] for i in h]

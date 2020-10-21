# 2nd attempt
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = [] # max heap
        self.right = [] # min heap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.left) == 0:
            self.left.append(-num)
        elif len(self.left) != len(self.right): # odd
            max_left = -self.left[0]
            if num < max_left:
                heapq.heappop(self.left)
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, max_left)
            else:
                heapq.heappush(self.right, num)
        else:
            min_right = self.right[0]
            if num < min_right:
                heapq.heappush(self.left, -num)
            else:
                heapq.heappop(self.right)
                heapq.heappush(self.left, -min_right)
                heapq.heappush(self.right, num)
            

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) != len(self.right): #odd
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0])/2.0
            
            
            
# First attempt
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num_items = 0
        self.midpoint = None
        self.left = [] # max heap
        self.right = [] # min heap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #print num
        #print self.num_items
        #print self.midpoint
        #print self.left
        #print self.right
        #print '---'
        if self.num_items == 0:
            self.midpoint = num
            self.num_items += 1
            return
            
        if self.num_items % 2: # currently odd
            if self.midpoint is not None and num < self.midpoint:
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, self.midpoint)
            elif self.midpoint is not None and num >= self.midpoint:
                heapq.heappush(self.left, -self.midpoint)
                heapq.heappush(self.right, num)
                
            self.midpoint = None
        else: # currently even  
            if num >= -self.left[0] and num <= self.right[0]:
                self.midpoint = num
            elif num < -self.left[0]:
                self.midpoint = -heapq.heappop(self.left)
                heapq.heappush(self.left, -num)
            else:
                self.midpoint = heapq.heappop(self.right)
                heapq.heappush(self.right, num)
        
        self.num_items += 1

    def findMedian(self):
        """
        :rtype: float
        """
        #print self.num_items
        #print self.midpoint
        #print self.left
        #print self.right
        #print '---'
        if self.num_items % 2: # currently odd
            return self.midpoint
        else:
            return (-self.left[0] + self.right[0])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

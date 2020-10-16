# Brute force approach
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # empty array
        # possible target is not found
        # [x]
        start = end = -1
        found = False
        for i in range(len(nums)):
            if nums[i] == target and found == False:
                start = i
                found = True
            if nums[i] != target and found == True:
                end = i - 1
                break
            if i == len(nums)-1 and found == True:
                end = i 
        
        return [start, end]
        
# Binary search approach
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0: return [-1, -1]
        start = end = -1
        
        # find starting position
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid + 1
            else:
                r = mid
        
        if nums[r] != target:
            return [start, end]
        else:
            start = r
        
        # find ending position
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r+1)//2    # we want a ceiling instead
            if nums[mid]<=target:
                l = mid 
            else:
                r = mid -1
        
        return [start, r]
                

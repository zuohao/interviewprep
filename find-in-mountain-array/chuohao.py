# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def __init__(self):
        self.cache = {}
        
    def cache_get(self, idx, mountain_arr):
        if idx not in self.cache:
            self.cache[idx] = mountain_arr.get(idx)
        return self.cache[idx]
    
    def find_peak_idx(self, mountain_arr):
        left = 0
        right = mountain_arr.length() - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.cache_get(mid, mountain_arr) < self.cache_get(mid+1, mountain_arr):
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(self, start, end, target, mountain_arr, asc = True):
        left = 0
        right = end
        while left <= right:
            mid = left + (right - left) // 2
            if self.cache_get(mid, mountain_arr) == target:
                return mid
            elif asc:
                if self.cache_get(mid, mountain_arr) < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if self.cache_get(mid, mountain_arr) < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
    
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        peak_idx = self.find_peak_idx(mountain_arr)
        idx = self.binary_search(0, peak_idx, target, mountain_arr)
        if idx == -1:
            idx = self.binary_search(peak_idx+1, mountain_arr.length()-1, target, mountain_arr, asc = False)
        return idx

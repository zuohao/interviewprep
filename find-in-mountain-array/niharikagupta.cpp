/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findBitonicPoint(MountainArray &mountainArr, int lo, int hi){
        if(lo>hi)
            return -1;
        if(lo==hi){
            return lo;
        }
        int mid = (lo+hi)/2;
        if(mid-1>=0 && mountainArr.get(mid)>mountainArr.get(mid-1) && mountainArr.get(mid)>mountainArr.get(mid+1))
            return mid;
        else if(mountainArr.get(mid)<mountainArr.get(mid+1))
            return findBitonicPoint(mountainArr,mid+1,hi);
        else
            return findBitonicPoint(mountainArr,lo,mid-1);
    }
    
    int binSearch(int target, MountainArray &mountainArr, bool isAsc, int lo, int hi){
        if(lo>hi)
            return -1;
        if(lo==hi)
            return mountainArr.get(lo)==target?lo:-1;
        int mid = (lo+hi)/2;
        if(target==mountainArr.get(mid))
            return mid;
        if(isAsc){
            if(target<mountainArr.get(mid))
                return binSearch(target,mountainArr, isAsc,lo,mid-1);
            else
                return binSearch(target,mountainArr, isAsc,mid+1,hi);
        }else{
            if(target<mountainArr.get(mid))
                return binSearch(target,mountainArr, isAsc,mid+1,hi);
            else
                return binSearch(target,mountainArr, isAsc,lo,mid-1);
        }
        
    }
    
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int peakIndex = findBitonicPoint(mountainArr,0,mountainArr.length()-1);
        int searchIndex = binSearch(target,mountainArr,true,0,peakIndex);
        if(searchIndex != -1)
            return searchIndex;
        return binSearch(target,mountainArr,false,peakIndex+1,mountainArr.length()-1);
    }
};

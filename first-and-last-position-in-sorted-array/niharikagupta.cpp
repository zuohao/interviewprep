class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n=nums.size();
        vector<int> res(2,-1);
        
        int left = binSearch(0,n,true,nums,target);
        if(left>=n || nums[left]!=target)
            return res;
        
        res[0] = left;
        res[1] = binSearch(0,n,false,nums,target)-1;
        
        return res;
    }
    
    int binSearch(int low, int high, bool flag, vector<int> &nums, int target){
        while(low<high){
            
            int mid = low + (high-low)/2;
            if(nums[mid]>target || (flag && nums[mid]==target)){
                high=mid;
            }
            else
                low=mid+1;
        }
        return low;
    }
};

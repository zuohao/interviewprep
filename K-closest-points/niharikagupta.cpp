class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
       int len=points.size();
        int l=0;
        int r=len-1;
        
        while(l<=r){
            int mid = quickselect(points,l,r);
            if(mid==k) break;
            if(mid<k) l=mid+1;
            else r=mid-1;
        }
        return vector<vector<int>>(points.begin(), points.begin() + k);
    }
    int quickselect(vector<vector<int>>& A, int l, int r){
        vector<int> pivot = A[l];
        while(l<r){
            while(l<r && compare(A[r],pivot)>=0)r--;
            A[l]=A[r];
            while (l < r && compare(A[l], pivot) <= 0) l++;
            A[r] = A[l];
        }
        A[l]=pivot;
        return l;
        
    }
    //(x1-x2)^2+(y1-y2)^2, x2=0,y2=0. So formula: x1^2+y1^2
    int compare(vector<int> p1, vector<int> p2){
        return p1[0] * p1[0] + p1[1] * p1[1] - p2[0] * p2[0] - p2[1] * p2[1];
    }
};

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int maxSum = INT_MIN;
        maxGain(root, maxSum);
        return maxSum;
    }
    int maxGain(TreeNode* root, int &maxSum){
        if(root==NULL) return 0;
        
        int leftGain = max(maxGain(root->left,maxSum),0);
        int rightGain = max(maxGain(root->right,maxSum),0);
        
        maxSum = max(maxSum,leftGain+rightGain+root->val);
        
        return root->val+max(leftGain,rightGain);
    }
};

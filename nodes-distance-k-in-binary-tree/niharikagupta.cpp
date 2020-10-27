/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        vector<int> res;
        dfs(root,target,K,res);
        return res;
    }
    
    int dfs(TreeNode* node, TreeNode* target, int k,vector<int> &res){
        if(node == NULL)
            return -1;
        if(node == target){
            distK(node,res,k);
            return 1;
        }
        else{
            int left = dfs(node->left,target,k,res);
            int right = dfs(node->right,target,k,res);
            
            if(left!=-1){
                if(left==k) res.push_back(node->val);
                distK(node->right,res,k-left-1);
                return left+1;
            }
            else if(right!=-1){
                if(right==k) res.push_back(node->val);
                distK(node->left,res,k-right-1);
                return right+1;
            }
            else{
                return -1;
            }
        }
            
    }
    void distK(TreeNode* node, vector<int> &res, int k){
        if(node==NULL) return;
        if(k==0)
            res.push_back(node->val);
        else{
            distK(node->left,res,k-1);
            distK(node->right,res,k-1);
        }
        
    }
};

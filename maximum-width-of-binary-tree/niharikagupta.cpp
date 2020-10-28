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
    int widthOfBinaryTree(TreeNode* root) {
        if(root==NULL)
            return 0;
        unsigned long long maxWidth=0;
        queue<pair<TreeNode*,unsigned long long>> q;// Indexing scheme: Ci->2*Ci+1, 2*Ci+2
        q.push({root,0});
        
        while(!q.empty()){
            int len = q.size();
            pair<TreeNode*, unsigned long long> p;
            unsigned long long firstIndex = 0;
            
            for(int i=0;i<len;i++){
                p = q.front();
                if(i==0)
                    firstIndex=p.second;
                q.pop();
                
                if (p.first->left != NULL)
                    q.push({p.first->left,2*p.second});
                if (p.first->right != NULL)
                    q.push({p.first->right,2*p.second+1});
            }
            maxWidth=max(maxWidth,(p.second-firstIndex+1));
        }
        return maxWidth;
    }
};

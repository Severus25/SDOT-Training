#Leetcode - 114
class Solution {
public:
    TreeNode* pre=NULL;
    void flatten(TreeNode* root) {
        if(!root){return;}
        flatten(root->right);
        flatten(root->left);
        root->right=pre;
        root->left=NULL;
        pre=root;   
    }
};

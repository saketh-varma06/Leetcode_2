# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans=[]
        if root is None:
            return []
        def solve(root,level):
            if root is None:
                return 
            if len(ans)==level:
                ans.append([])
            if level%2==0:
                ans[level].append(root.val)
            else:
                ans[level].insert(0,root.val)
            solve(root.left,level+1)
            solve(root.right,level+1)
        solve(root,0)
        return ans
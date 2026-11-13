# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans=[]
        if root is None:
            return []
        part=[root.val]
        if root.left is None and root.right is None:
            if sum(part)==targetSum:
                ans.append(part)
            return ans
        left=self.pathSum(root.left,targetSum-root.val)
        for i in left:
            ans.append(part+i)
        right=self.pathSum(root.right,targetSum-root.val)
        for i in right:
            ans.append(part+i)
        return ans
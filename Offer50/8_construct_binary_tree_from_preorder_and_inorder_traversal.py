""" [利用前序和中序遍历的结果构造二叉树](https://www.lintcode.com/problem/construct-binary-tree-from-preorder-and-inorder-traversal/description?_from=ladder&&fromId=6)
"""


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def constuct_binary_tree(self, preorder: list, inorder: list):
        if not (preorder and inorder):
            return None
        val = preorder[0]
        for index, num in enumerate(inorder):
            if num == val:
                break
        root = TreeNode(val)
        root.left = self.constuct_binary_tree(preorder[1: index + 1], inorder[:index])
        root.right = self.constuct_binary_tree(preorder[index + 1:], inorder[index + 1:])
        return root

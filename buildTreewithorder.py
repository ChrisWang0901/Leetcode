class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def buildTreeHelper(preorder, inorder, l, r):
            nonlocal i
            if l > r:
                return
            node = TreeNode(preorder[i])

            mid = inorder.index(node.val)
            i += 1

            node.left = buildTreeHelper(preorder, inorder, l, mid - 1)
            node.right = buildTreeHelper(preorder, inorder, mid + 1, r)

            return node
        i = 0
        return buildTreeHelper(preorder, inorder, 0, len(inorder) - 1)

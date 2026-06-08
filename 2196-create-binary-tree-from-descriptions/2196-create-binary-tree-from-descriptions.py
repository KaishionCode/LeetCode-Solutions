# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        for parent_val, children_val, is_left in descriptions:
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if children_val not in nodes:
                nodes[children_val] = TreeNode(children_val)
            if is_left == 1:
                nodes[parent_val].left = nodes[children_val]
            else: 
                nodes[parent_val].right = nodes[children_val]
            children.add(children_val)
        for i in nodes:
            if i not in children:
                return nodes[i]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
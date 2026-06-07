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
        
        # Bước 1: Duyệt qua các mô tả để tạo node và liên kết chúng
        for parent_val, child_val, is_left in descriptions:
            # Nếu node cha/con chưa tồn tại, ta tạo mới và lưu vào dictionary
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            
            # Liên kết node con vào node cha tùy thuộc vào is_left
            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
                
            # Ghi nhận node con vào set
            children.add(child_val)
            
        # Bước 2: Tìm Node gốc (Root)
        # Root là node duy nhất không xuất hiện trong tập hợp 'children'
        for val in nodes:
            if val not in children:
                return nodes[val]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
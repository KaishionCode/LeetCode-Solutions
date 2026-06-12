from collections import deque
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Suy ra n từ số lượng cạnh (Tree properties: Vertices = Edges + 1)
        n = len(edges) + 1
        
        # Bước 1: Dựng danh sách kề
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Tính số lượng bước nhảy tối đa cho Binary Lifting
        LOG = n.bit_length()
        depth = [0] * (n + 1)
        up = [[0] * LOG for _ in range(n + 1)]
        
        # Bước 2: Dùng BFS để tính độ sâu (depth) và dựng mảng tổ tiên (up)
        queue = deque([1])
        depth[1] = 0
        up[1][0] = 0
        
        visited = [False] * (n + 1)
        visited[1] = True
        
        while queue:
            u = queue.popleft()
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    
                    # Cập nhật bảng Binary Lifting cho node v
                    for j in range(1, LOG):
                        if up[v][j - 1] != 0:
                            up[v][j] = up[up[v][j - 1]][j - 1]
                        else:
                            break
                            
                    queue.append(v)
                    
        # Hàm tìm tổ tiên chung gần nhất (LCA)
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]
        
        # Bước 3: Xử lý các truy vấn
        ans = []
        for u, v in queries:
            lca = get_lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[lca]
            
            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow(2, dist - 1, MOD))
                
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
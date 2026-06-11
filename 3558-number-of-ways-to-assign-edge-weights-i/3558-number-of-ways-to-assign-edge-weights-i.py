import collections
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        if n == 1:
            return 0
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        queue = collections.deque([(1, 0)]) 
        visited = {1}
        max_depth = 0
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
        MOD = 10**9 + 7
        if max_depth == 0:
            return 0
        return pow(2, max_depth - 1, MOD)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
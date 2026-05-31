class trienode:
    def __init__(self,best_char):
        self.children = {}
        self.best_char = best_char
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        chuoi_ngan_nhat = 0
        for i in range (1,len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[chuoi_ngan_nhat]):
                chuoi_ngan_nhat = i

        goc = trienode(chuoi_ngan_nhat)

        for i,word in enumerate(wordsContainer):
            curr = goc
            for char in word[::-1]:
                if char not in curr.children:
                    curr.children[char] = trienode(i)
                else:
                    vi_tri_tam = curr.children[char].best_char
                    if len(word) < len(wordsContainer[vi_tri_tam]):
                        curr.children[char].best_char = i
                curr = curr.children[char]
        ketqua = []
        for word in wordsQuery:
            curr = goc
            for char in word[::-1]:
                if char in curr.children:
                    curr = curr.children[char]
                else: break
            ketqua.append(curr.best_char)
        return ketqua



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
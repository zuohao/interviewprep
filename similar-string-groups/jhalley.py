class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def calcValidDistance(a, b):
            current_score = 0
            if a == b: return True
            for i in range(word_length):
                if a[i] != b[i]:
                    current_score += 1
                    if current_score > 2:
                        return False
            return True
            
            
        group_count = 0
        word_length = len(A[0])
        A = set(A)
        
        while len(A) > 0:
            group_count += 1
            curr_words = [A.pop()]
            while len(curr_words) > 0:
                curr_word = curr_words.pop()
                for check in [i for i in product([curr_word],A)]:
                    if check[1] not in A: 
                        continue
                    if calcValidDistance(check[0], check[1]):
                        curr_words.append(check[1])
                        A.remove(check[1])
                        
        
        return group_count
            

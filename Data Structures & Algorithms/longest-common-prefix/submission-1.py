class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_sorted = sorted(strs, key=len, reverse=False)
        result = ""
        for index, char in enumerate(strs_sorted[0]):
            for i in range(1, len(strs_sorted)):
                word = strs_sorted[i]
                if char != word[index]:
                    return result
            else:
                result += char    
    
                
        return result 
        
        
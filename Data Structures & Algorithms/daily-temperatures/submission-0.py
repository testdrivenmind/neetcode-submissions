class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index_store = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while index_store and temperatures[i] > temperatures[index_store[-1]]:
                prev_index = index_store.pop()
                result[prev_index] = i - prev_index
            index_store.append(i)
        return result
        
             
        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_index_stack = [] # to store indices of temperature whose warmer days are not known
        result = [0] * len(temperatures) # # initiating all with zero else when to over-write later we will list of index out of range error


        for index, temp in enumerate(temperatures):
            while temp_index_stack and temperatures[index] > temperatures[temp_index_stack[-1]]:
                prev_index = temp_index_stack.pop()
                result[prev_index] = index - prev_index
            temp_index_stack.append(index)
        return result
        
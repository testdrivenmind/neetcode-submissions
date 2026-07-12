class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp_stack = [] # store indices of warm temeratures which we dont know

        for index, temp in enumerate(temperatures):
            while temp_stack and temp > temperatures[temp_stack[-1]]:
                prev_index = temp_stack.pop()
                result[prev_index] = index - prev_index
            temp_stack.append(index)
        return result
        



        
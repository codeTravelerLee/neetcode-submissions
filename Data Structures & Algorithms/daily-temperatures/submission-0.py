class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stack = []
        result = [0] * length

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = i - previous_index

            stack.append(i)

        return result

        
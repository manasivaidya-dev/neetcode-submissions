class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        result = [0] * (len(temperatures))
        for i in range(len(temperatures)):
            if len(temp_stack) == 0:
                temp_stack.append(i)
            else:
                #temp_stack[len(temp_stack) - 1] -- index
                while temp_stack and temperatures[temp_stack[len(temp_stack) - 1]] < temperatures[i]:
                    day_index = temp_stack[len(temp_stack) - 1]
                    temp_stack.pop()
                    result[day_index] = i - day_index
                    print(result)
                temp_stack.append(i)
        return result


        
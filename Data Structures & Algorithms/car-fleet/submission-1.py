class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_arr = []
        for i in range(len(position)):
            new_arr.append((position[i], speed[i]))

        new_arr.sort(key=lambda x: x[0], reverse=True)
        fleets = 0
        max_time = 0
        for i in range(len(position)):
            time = (target - new_arr[i][0])/new_arr[i][1]
            if time > max_time:
                fleets += 1
                max_time = time
       
        return fleets
        
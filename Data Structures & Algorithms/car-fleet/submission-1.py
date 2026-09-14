class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        cars = [[p, s] for p, s in zip(position, speed)]

        for p, s in sorted(cars)[::-1]:
            time = (target - p) /s

            if not st or time > st[-1]:
                st.append(time)
        
        return len(st)
        
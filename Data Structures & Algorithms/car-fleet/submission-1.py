class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        f = 0;
        last_time = -1

        for pos, spd in cars:
            time = (target - pos) / spd
            
            if time > last_time:
                f+=1
                last_time = time

        return f
        
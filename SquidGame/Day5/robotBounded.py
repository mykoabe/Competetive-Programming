class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # if direction
        # 0: north, 1: east, 2: south, 3: west
        start, direction = [0, 0], 0
        for instruction in instructions:
            if instruction == "L":
                direction = (direction + 3) % 4
            elif instruction == "R":
                direction = (direction + 1) % 4
            elif instruction == "G":
                if direction == 0:
                    start[1] += 1
                elif direction == 1:
                    start[0] += 1
                elif direction == 2:
                    start[1] -= 1
                elif direction == 3:
                    start[0] -= 1
        return (start == [0, 0]) or direction != 0

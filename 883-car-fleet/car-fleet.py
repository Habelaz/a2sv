class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p,s in zip(position,speed)]
        stack = []
        cars.sort(reverse = True)
        # print(cars)
        for p,s in cars:
            stack.append((target-p)/s)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
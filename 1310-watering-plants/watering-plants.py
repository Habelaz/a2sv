class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count = 0
        nc = capacity

        for i, water in enumerate(plants):
            if nc < water:
                count += 2 * i
                nc = capacity
            nc -= water
            count += 1

        return count
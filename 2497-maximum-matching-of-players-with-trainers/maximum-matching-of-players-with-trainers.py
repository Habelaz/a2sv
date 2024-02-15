class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count = 0
        pla_ptr = 0
        tra_ptr = 0
        players.sort()
        trainers.sort()
        n = min(len(players),len(trainers))
        while pla_ptr < len(players) and tra_ptr < len(trainers):
            if players[pla_ptr] <= trainers[tra_ptr]:
                count += 1
                pla_ptr += 1
                tra_ptr += 1
            elif trainers[tra_ptr] < players[pla_ptr]:
                tra_ptr += 1
        return count
        
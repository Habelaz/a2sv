class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losses = {}

        for w,l in matches:
            winners.add(w)
            if l in losses:
                losses[l] += 1
            else:
                losses[l] = 1
        no_losses = [p for p in winners if p not in losses]
        one_loss = []
        for player, loss_count in losses.items():
            if loss_count == 1:
                one_loss.append(player)
        no_losses.sort()
        one_loss.sort()
        return [no_losses,one_loss]
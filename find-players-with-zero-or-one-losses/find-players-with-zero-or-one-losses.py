class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # create a set for seen players and count their loss
        seen = set()
        loss_count = {}

        # iterate through the matches and keep track of the losses
        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            loss_count[loser]= loss_count.get(loser,0) + 1
        
        zero_loss = []
        one_loss = []
        for player in seen:
            count = loss_count.get(player,0)
            if count ==0:
                zero_loss.append(player)
            elif count ==1:
                one_loss.append(player)

        return[sorted(zero_loss), sorted(one_loss)]
        
        
        
        
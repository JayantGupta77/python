class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        
        i = 0  
        j = 0  
        matches = 0
        
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                # We can match this player with this trainer
                matches += 1
                i += 1
                j += 1
            else:
                # Current trainer can't handle this player, try next trainer
                j += 1
        
        return matches

        
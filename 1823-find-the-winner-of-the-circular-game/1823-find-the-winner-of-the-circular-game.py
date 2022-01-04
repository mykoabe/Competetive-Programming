class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        friends = [i for i in range(1, n+1)]

        def helper(friends, idx=0):
            if len(friends) == 1:
                return friends[0]

            pop_idx = (idx + k - 1)%len(friends)

            friends.pop(pop_idx)
            
            return helper(friends, pop_idx)

        return helper(friends)
        
    
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        dp = [0 for _ in range(len(players))]
        for i in range(len(players)):
            dp[i] = players[i][1]
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        return max(dp)
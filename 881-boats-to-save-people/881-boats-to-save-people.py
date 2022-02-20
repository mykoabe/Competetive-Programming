class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        a=sorted(people)
        i=0
        j=len(people)-1
        count=0
        while i<=j:
            if a[i]+a[j]<=limit:
                count+=1
                i+=1
                j-=1
            else:
                count+=1
                j-=1
        return count
        
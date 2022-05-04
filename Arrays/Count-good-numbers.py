class Solution:
    def countGoodNumbers(self, n: int) -> int:
        d = 10**9+7
        
        if n%2==0:
            even_place = n//2
        else:
            even_place = (n+1)//2
            
        odd_place = n//2

        even_place_combinations = pow(5,even_place,d)      
        prime_place_combinations = pow(4,odd_place,d)
        
        return (even_place_combinations*prime_place_combinations)%d
        

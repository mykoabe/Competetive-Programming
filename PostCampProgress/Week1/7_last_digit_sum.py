class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#         if len(digits) == 0:
#             return [1]
#         if digits[-1] != 9:
#             digits[-1] += 1
#             return digits
#         else: # example [9, 9]
#             digits[-1] = 0
#             return self.plusOne(digits[:-1]) + [0]
            
        
        res, mul = 0, 1
        for num in digits[::-1]:
            res += num * mul
            mul *= 10
        res += 1
        return list(str(res))
            
        
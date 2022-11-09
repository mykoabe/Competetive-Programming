class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        # sort quantity to reduce the backtracking calls
        quantity.sort(reverse=True)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        # here we have to sort based on freq values becuase for example if we have 2 numbers with 
        # frequency 3 and 2 numbers with frequency 2, we can distribute 3 numbers with frequency 
        # 3 first and then 2 numbers with frequency 2. so this reduces the number of backtracking
        #  calls
        
        freq = sorted(freq.values(), reverse=True)
        def backtrack(index, path):
            if index == len(quantity): # if we have distributed all the numbers
                return True
            for j in range(len(path)): # try to distribute quantity[i] to each path[j]
                if path[j] >= quantity[index]: # if we can distribute quantity[i] to path[j]
                    path[j] -= quantity[index]
                    if backtrack(index+1, path): # try to distribute quantity[i+1] to path
                        return True
                    path[j] += quantity[index]
            if len(path) < len(freq) and freq[index] >= quantity[index]:  # if we can distribute quantity[i] to a new path
                path.append(freq[index] - quantity[index]) 
                if backtrack(index+1, path):
                    return True
                path.pop()
            return False
        return backtrack(0, [])
        # TODO: this solution works for the first 7 test cases but fails for the 8th test case. I need to figure out why it fails for the 8th test case
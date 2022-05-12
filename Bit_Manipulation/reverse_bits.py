class Solution:
    def reverseBits(self, n: int) -> int:
        
        bits = '{:032b}'.format(n)
        reversed_bits = bits[::-1]
        reversed_number = int(reversed_bits, 2)
        
        return reversed_number

        
        
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        self.digits = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens2 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["Thousand", "Million", "Billion"]
        self.res = ""
        self.helper(num)
        return self.res.strip()
    
    def helper(self, num):
        if num == 0:
            return
        if num < 10:
            self.res += self.digits[num-1] + " "
        elif num < 20:
            self.res += self.tens[num-10] + " "
        elif num < 100:
            self.res += self.tens2[num//10-2] + " "
            self.helper(num%10)
        elif num < 1000:
            self.res += self.digits[num//100-1] + " Hundred "
            self.helper(num%100)
        else:
            for i in range(len(self.thousands)):
                if num < 1000**(i+2):
                    self.helper(num//1000**(i+1))
                    self.res += self.thousands[i] + " "
                    self.helper(num%1000**(i+1))
                    break
    
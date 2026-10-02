class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = 0
        while True:
            cur = len(digits) - i - 1
            if digits[cur] == 9:
                digits[cur] = 0
                if cur == 0:
                    digits.insert(1, 0)
            else:
                digits[cur] += 1
                break;
            i+=1
        return digits;
            
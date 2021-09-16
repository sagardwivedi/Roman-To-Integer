class Solution:
    def romanToInt(self, s: str) -> int:
        Roman_dict = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev = "I"
        total = 0
        for i in s[::-1]:
            if Roman_dict[i] >= Roman_dict[prev]:
                total += Roman_dict[i]
                prev = i
            else:
                total -= Roman_dict[i]
        return total

a = Solution()
print(a.romanToInt("IV"))

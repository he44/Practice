"""
Integer to Roman
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        units = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        unit_to_sym = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        ans = ''
        n = num
        for unit in units:
            #  check if we have this char
            x = n // unit
            y = n % unit
            for i in range(x):
                ans = ans + unit_to_sym[unit]
            n = y
        return ans

def main():
    s = Solution()
    test_cases = [3,4,9,58,1994]
    for number in test_cases:
        roman = s.intToRoman(number)
        print("%d is %s"%(number, roman))


if __name__ == "__main__":
    main()

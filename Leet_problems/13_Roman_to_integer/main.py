"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Example 4
Input: s = "XLIX"
Output: 49
Explanation: XL = 50 - 10, IX = 10 - 1.

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution:
    def __init__(self, s: str):
        self.s = s

    # TODO get input string as user input
    def roman_to_int(self) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0

        if len(self.s) == 1:
            integer += romans[self.s[0]]
            print(f"simple IF --- Roman 0 {romans[self.s[0]]} --- Sum {integer}")
        elif len(self.s) > 1:
            for index in range(len(self.s) - 2):
                print(f"LOOP INDEX {index}")
                if romans[self.s[index]] < romans[self.s[index + 1]]:  # IX
                    integer += romans[self.s[index + 1]] - romans[self.s[index]]
                    print(f" x < y --- Index {index} --- Roman I {romans[self.s[index]]} --- "
                          f"Roman I + 1 {romans[self.s[index + 1]]} --- Sum {integer}")
                elif romans[self.s[index-1]] >= romans[self.s[index]] >= romans[self.s[index + 1]]:  # XII, XVI
                    integer += romans[self.s[index]]
                    print(f" x > y --- Index {index} --- Roman I {romans[self.s[index]]} ---"
                          f" Sum {integer}")
                elif romans[self.s[index-1]] < romans[self.s[index]] > romans[self.s[index+1]]:  # XLI
                    print(f"a < x < y --- pass")

            if romans[self.s[-2]] < romans[self.s[-1]]:
                integer += romans[self.s[-1]] - romans[self.s[-2]]
                print(f"LAST TWO -2 < -1 --- Roman -2 {romans[self.s[-2]]} --- Roman -1 {romans[self.s[-1]]} --- Sum {integer}")
            else:
                integer += romans[self.s[-2]] + romans[self.s[-1]]
                print(f"LAST TWO ELSE --- Roman -2 {romans[self.s[-2]]} --- Roman -1 {romans[self.s[-1]]} --- Sum {integer}")
        return integer

test = Solution("LVIII")
print(test.roman_to_int())

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
#
# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
# Example 4
# Input: s = "XLIX"
# Output: 49
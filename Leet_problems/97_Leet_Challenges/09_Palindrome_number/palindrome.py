"""
Given an integer x, return true if x is a
palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore, it is not a palindrome.
"""


class Number:
    def __init__(self, x: int):
        self.x = x

    def is_palindrome(self) -> bool:
        if self.x < 0:
            return False
        else:
            str_x = str(self.x)
            # TODO Could you solve it without converting the integer to a string?
            if str_x == str_x[::-1]:
                return True
        return False


"""
Leet code solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        y = list(str(x))
        y.reverse()
        y1 = "".join(y)
        return(bool(z==y1))
"""

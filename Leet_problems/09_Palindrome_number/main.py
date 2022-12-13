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
import random

class Solution:
    def __init__(self, x: int):
        self.x = x

    def is_palindrome(self) -> bool:
        if self.x < 0:
            return False
        else:
            str_x = str(self.x)
            #TODO Could you solve it without converting the integer to a string?
            if str_x[::] == str_x[::-1]:
                return True
        return False

test1 = Solution(-121)
test2 = Solution(0)
test3 = Solution(10)
test4 = Solution(121)
test5 = Solution(1001)
test6 = Solution(random.randint(-100, 1000000))

print(f"test1 ({test1.x}) - {test1.is_palindrome()}\n"
      f"test2 ({test2.x}) - {test2.is_palindrome()}\n"
      f"test3 ({test3.x}) - {test3.is_palindrome()}\n"
      f"test4 ({test4.x}) - {test4.is_palindrome()}\n"
      f"test5 ({test5.x}) - {test5.is_palindrome()}\n"
      f"test6 ({test6.x}) - {test6.is_palindrome()}\n")

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

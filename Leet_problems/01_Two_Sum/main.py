"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add
up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.1

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

"""


class Solution:

    """
    Init method initializes the attributes and defines instances??
    """
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    """
    With current implementation we dont need to pass parameters into two_sum method as it takes them from __init__
    """
    #TODO Can you come up with an algorithm that is less than O(n2) time complexity?
    def two_sum(self):
        answer = []

        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[j] == self.target - self.nums[i]:
                    answer.append(i)
                    answer.append(j)
                    return answer


# Assign class to anything 2
test = Solution([2, 11, 7, 3], 9)

# Call the method two_sum on test instance
print(test.two_sum())

class NumList:
    def __init__(self, nums: list, target: int) -> None:
        self.nums = nums
        self.target = target

    def two_sum(self) -> list[int]:
        answer = []

        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[j] == self.target - self.nums[i]:
                    answer.append(i)
                    answer.append(j)
                    return answer

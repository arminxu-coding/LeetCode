"""
295. 数据流的中位数
https://leetcode.cn/problems/find-median-from-data-stream/description/?envType=study-plan-v2&envId=top-100-liked
"""


class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        index = 0
        for item in self.nums:
            if item < num:
                index += 1
            else:
                break
        self.nums.insert(index, num)

    def findMedian(self) -> float:
        length = len(self.nums)
        mid = length // 2
        if length % 2 == 0:
            return (self.nums[mid - 1] + self.nums[mid]) / 2
        return float(self.nums[mid])


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())

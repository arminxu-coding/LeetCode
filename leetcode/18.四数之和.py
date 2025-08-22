"""
18. 四数之和
https://leetcode.cn/problems/4sum/description/
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        length = len(nums)
        nums.sort()
        # 四指针遍历，确定两个指针，再用另外两个指针
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # 当前数和前一个一样的话，那么作为第一个 之前已经存在了，那么数值一定是相同的，去重
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 1] + nums[length - 2] + nums[length - 3] < target:
                continue
            # 确定第二个指针
            for j in range(i + 1, length - 2):
                # 判断第二个是否也是重复的，可以去重
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 1] + nums[length - 2] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    # 计算当前四个值相加
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif sum > target:
                        right -= 1
                    else:
                        left += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
    print(solution.fourSum(nums=[2, 2, 2, 2, 2], target=8))

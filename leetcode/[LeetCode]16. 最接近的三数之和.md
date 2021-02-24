# [LeetCode]16. 最接近的三数之和

## 题目

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

### 示例 1

```bash
输入：nums = [-1,2,1,-4], target = 1

输出：2
```

> 与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

## 解析

- 分析

1. 跟[15.三数之和](https://www.cnblogs.com/WilsonPan/p/14435168.html)类似

2. `abs(target - current)` 这个值越少说明越接近

- 算法流程

1. 排序 - 为了能使用双指针

2. 遍历
   1. 固定一位（i）， 左右指针指向下一位与最后一位（`left = i + 1` , `right = n - 1`）
   2. 按条件遍历左右指针
      1. i + left + right == 0 : 当前和`target`重合了，直接返回
      2. i + left + right < 0  : 结果偏少，需要增加结果 left++（数组排序后从左往右依次增大）
      3. i + left + right > 0  : 结果偏大，需要减少结果 right--

## 源码

```py
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        length = len(nums)
        res: int = nums[0] + nums[1] + nums[2]
        for i in range(length-2):
            left = i + 1
            right = length - 1
            while left < right:
                total = (nums[i] + nums[left] + nums[right])
                if abs(target - total) < abs(target - res):
                    res = total

                if target == total:
                    return total
                elif total > target:
                    right = right - 1
                else:
                    left = left + 1

        return res
```

## 引用

[LeetCode - 16. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest)

[源码 - GitHub](https://github.com/WilsonPan/leetcode/blob/main/16.%E6%9C%80%E6%8E%A5%E8%BF%91%E7%9A%84%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.py)

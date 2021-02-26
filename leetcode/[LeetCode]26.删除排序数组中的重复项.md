# [LeetCode]26.删除排序数组中的重复项

## 题目

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

### 示例 1

```bash
输入:  [1,1,2]

输出:   2   #[1, 2]
```

### 示例 2

```bash
输入:   [1, 2, 2, 2, 3] 

输出:   3 #[1, 2, 3]

```

## 解析

- 难点

1. 原地替换，不能使用格外空间

- 算法流程

1. 特判 --> 小于2的数组，返回本身
2. 指针指向前两位（current, next = 0, 1)
3. 遍历比较current 与 next
   1. current == next : 相邻相同，next = next + 1
   2. current != next
      1. 若 next - current > 1: next 与 current 大于1，将next置换current `nums[current + 1] = nums[next]`
      2. next = next + 1

## 源码

- 解法一

```py
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        current, next = 0, 1

        while next < len(nums):
            if nums[current] != nums[next]:
                current = current + 1
                nums[current] = nums[next] if (next - current) > 0 else nums[current]
            next = next + 1
            pass

        return current + 1
```

## 引用

[LeetCode - 26.删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/)

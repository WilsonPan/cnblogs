# [LeetCode]31.下一个排列

## 题目

实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

### 示例 1

```bash
输入：nums = [1,2,3]
输出：[1,3,2]
```

### 示例 2

```bash
输入：nums = [3,2,1]
输出：[1,2,3]
```

## 解析

最好自己在纸画一下4个数的字典排序，就会发现`下一队列`如下规律

1. 第一个队列升序排序
2. 从右往前交换，当后面数列整个倒序时，需要往前升一位
3. 往前升一位后，后面的队列是升序排列
4. 需要升序情况(假设 i 需要升一位，k 是所需的数字)
   1. 这个时候`[i + 1, n]`倒序排列
   2. 因为这个时候`[i + 1, n]`倒序，替换i , k位置，并把队列反转就是需要的下一队列

- 难点

1. 不能使用额外空间

- 算法流程

1. 特判
   1. 数组长度小于2 : 直接返回
   2. 数组长度 == 2 或者 倒数第二位 小于 倒数第一 : 交换最后两位数即可
2. 找到需要升位的位置`pointer`
3. 左右指针遍历
   1. 右边第一个大于`nums[i]`或左边最后一个大于`nums[i]`即需要升位的数字
   2. 替换左右指针位置（反转队列）

## 源码

```py
from typing import List, Literal


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums or len(nums) <= 1:
            return

        length = len(nums)

        if length == 2 or nums[length - 2] < nums[length - 1]:
            nums[length - 2], nums[length - 1] = nums[length - 1], nums[length - 2]
            return

        pointer = length - 3
        while pointer >= 0:
            if nums[pointer] < nums[pointer + 1]:
                break
            pointer = pointer - 1

        left = pointer + 1
        right = length - 1
        current_val = nums[pointer] if pointer >= 0 else 101
        is_swap = False

        while left <= right:

            if not is_swap and nums[right] > current_val:
                nums[pointer], nums[right] = nums[right], nums[pointer]
                is_swap = True

            if not is_swap and nums[left] > current_val and nums[left + 1] <= current_val:
                nums[left], nums[pointer] = nums[pointer], nums[left]
                is_swap = True

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            pass
```

## 引用

[LeetCode - 31.下一个排列](https://leetcode-cn.com/problems/next-permutation/)

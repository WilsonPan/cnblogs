# LeetCode 15.三数之和

## 题目

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

### 示例 1

```bash
输入：nums = [-1,0,1,2,-1,-4]

输出：[[-1,-1,2],[-1,0,1]]
```

### 示例 2

```bash
输入：nums = []

输出：[]
```

### 示例 3

```bash
输入：nums = [0]

输出：[]
```

## 解析

- 难点
    1. 双指针
    2. 过滤重复

- 算法流程
  
1. 排序 - 为了能使用双指针

2. 特判
   1. 若第一位大于target, 直接返回，因为已经排序，后面只会越加越大

3. 遍历
   1. 过滤重复（同一个数字，第二次遍历）（`nums[i] == nums[i - 1]`) --> 保证第一个数字不重复
   2. 固定一位（i）， 左右指针指向下一位与最后一位（`left = i + 1` , `right = n - 1`）
   3. 按条件遍历左右指针
      1. i + left + right == 0 : 添加到结果集， 过滤左指针重复（保证第二个数不重复），过滤有指针（保证第三个数不重复）
      2. i + left + right < 0  : 结果偏少，需要增加结果 left++（数组排序后从左往右依次增大）
      3. i + left + right > 0  : 结果偏大，需要减少结果 right--

## 源码

```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1. sort
        2. specially
        3. for + two points (left = i + 1 , right = len - 1)
            3.1 nums[i] > 0     : return , because 
            3.2 i + left + right == 0   : add to res && skip same value
            3.3 i + left + right < 0    : left++
            3.4 i + left + right > 0    : right--
        """
        nums.sort()  # O(NlogN)


        n = len(nums)
        res: List[List[int]] = []

        for i in range(n):  # O(N)

            if nums[i] > 0:
                return res

            if(i > 0 and nums[i] == nums[i-1]):
                continue

            left = i + 1
            right = n - 1

            while (left < right):  # O(N)

                if (nums[i] + nums[left] + nums[right]) == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # skip same
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    # skip same
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif (nums[i] + nums[left] + nums[right]) < 0:
                    left = left + 1
                else:
                    right = right - 1
        return res
```

## 引用

[LeetCode - 15. 三数之和](https://leetcode-cn.com/problems/3sum/)

[源码 - GitHub](https://github.com/WilsonPan/leetcode/blob/main/15.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.py)

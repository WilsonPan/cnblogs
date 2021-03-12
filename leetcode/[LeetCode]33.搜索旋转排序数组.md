# [LeetCode]33.搜索旋转排序数组

## 题目

整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，`nums` 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标 从 0 开始 计数）。例如， `[0,1,2,4,5,6,7]` 在下标 3 处经旋转后可能变为 `[4,5,6,7,0,1,2]` 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的索引，否则返回 -1 。

**提示：**

- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- nums 中的每个值都 独一无二
- nums 肯定会在某个点上旋转
- -10^4 <= target <= 10^4

**进阶**：你可以设计一个时间复杂度为 `O(log n)` 的解决方案吗？

### 示例 1

```bash
输入：nums = [4,5,6,7,0,1,2], target = 0

输出：4
```

### 示例 2

```bash
输入：nums = [4,5,6,7,0,1,2], target = 3

输出：-1
```

## 解析

要不是看到进阶提示，我都以为看错题，找无序数组下标（nums 肯定会在某个点上旋转），第一时间想到遍历（`O(N)`)，优化一点双指针比遍历(`O(N/2)`)

看到`O(log n)`，自然会想到二分搜索，但是二分搜索通常是排序好数组，这里旋转后肯定不是排序好的数组，只能往旋转后的规律去找

- 难点

1. 时间复杂度为`O(log n)`算法

- 算法流程(二分搜索)


## 源码

- 遍历
  
```py
def search(self, nums: List[int], target: int) -> int:

    for i, num in enumerate(nums) if nums else []:

        if num == target:
            return i
    return -1
```

- 双指针遍历（竟然超过83.24%的python3提交）

```py
def search(self, nums: List[int], target: int) -> int:

    if not nums or len(nums) <= 0:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] == target or nums[right] == target:
            return left if nums[left] == target else right

        left, right = left + 1, right - 1

    return -1
```

- 二分搜索

```py
def search(self, nums: List[int], target: int) -> int:

    if not nums or len(nums) <= 0:
        return -1

    return self.__binary_search(nums=nums, target=target, left=0, right=len(nums) - 1)

def __binary_search(sefl, nums: List[int], target: int, left: int, right: int) -> int:

    if left > right:
        return -1

    mid = int((left + right) / 2)

    if nums[mid] == target:
        return mid

    if nums[left] == target:
        return left

    if nums[right] == target:
        return right

    if nums[left] <= nums[mid]:
        if (target >= nums[left] and target <= nums[mid]):
            return sefl.__binary_search(nums, target, left + 1, mid - 1)
        else:
            return sefl.__binary_search(nums, target, mid + 1, right - 1)
    else:
        if target >= nums[left] or target <= nums[mid]:
            return sefl.__binary_search(nums, target, left + 1, mid - 1)
        else:
            return sefl.__binary_search(nums, target, mid + 1, right - 1)
```  

## 引用

[LeetCode - 33.搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array)

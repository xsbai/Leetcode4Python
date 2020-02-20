# coding=utf-8

"""
4. 寻找两个有序数组的中位数

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

	nums1 = [1, 3]
	nums2 = [2]

	则中位数是 2.0
示例 2:

	nums1 = [1, 2]
	nums2 = [3, 4]

	则中位数是 (2 + 3)/2 = 2.5


"""

"""
解题方法：滑动窗口
用两个指针分别指向两个数组，比较指针下的元素大小，一共移动次数为 (m+n + 1)/2，便是中位数。
中位数指的是该数左右个数相等。
例如:
	nums1: [a1,a2,a3,...an]
	nums2: [b1,b2,b3,...bn]
	[nums1[:left1],nums2[:left2] | nums1[left1:], nums2[left2:]]
只要保证左右两边 个数 相同，中位数就在 | 这个边界旁边产生。

如何找边界值，我们可以用二分法，我们先确定 num1 取 m1 个数的左半边，那么 num2 取 m2 = (m+n+1)/2 - m1 的左半边，找到合适的 m1，就用二分法找。
当 [ [a1],[b1,b2,b3] | [a2,..an],[b4,...bn] ]

我们只需要比较 b3 和 a2 的关系的大小，就可以知道这种分法是不是准确的！
例如：我们令：
	nums1 = [-1,1,3,5,7,9]
	nums2 = [2,4,6,8,10,12,14,16]
	当 m1 = 4,m2 = 3 ,它的中位数就是median = (num1[m1] + num2[m2])/2
"""
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        k = (n1 + n2 + 1)//2
        left = 0
        right = n1
        while left < right :
            m1 = left +(right - left)//2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1 
        c1 = max(nums1[m1-1] if m1 > 0 else float("-inf"), nums2[m2-1] if m2 > 0 else float("-inf") )
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 <n2 else float("inf"))
        return (c1 + c2) / 2




if __name__ == '__main__':
    solution = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    print(solution.findMedianSortedArrays(nums1,nums2))
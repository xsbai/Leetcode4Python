# coding=utf-8

"""
1. 两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
	给定 nums = [2, 7, 11, 15], target = 9
	因为 nums[0] + nums[1] = 2 + 7 = 9
	所以返回 [0, 1]
"""

"""
解题关键num2 = target - num1，是否也在 list 中，那么就需要运用以下两个方法：
num2 in nums，返回 True 说明有戏
nums.index(num2)，查找 num2 的索引
"""
def twoSum1(nums, target):
    lens = len(nums)
    j=-1
    for i in range(lens):
        if (target - nums[i]) in nums:
            if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                continue
            else:
                j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2                
                break
    if j>0:
        return [i,j]
    else:
        return []

"""
在方法一基础上，num2 的查找并不需要每次从 nums 查找一遍，只需要从 num1 位置之前或之后查找即可。
但为了方便 index 这里选择从 num1 位置之前查找：
"""
def twoSum2(nums, target):
    lens = len(nums)
    j=-1
    for i in range(1,lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j>=0:
        return [j,i]


"""
通过字典来模拟哈希查询的过程。
个人理解这种办法相较于方法一其实就是字典记录了 num1 和 num2 的值和位置，
而省了再查找 num2 索引的步骤。
"""
def twoSum3(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]


"""
类似方法二，不需要 mun2 不需要在整个 dict 中去查找。
可以在 num1 之前的 dict 中查找，因此就只需要一次循环可解决。
"""
def twoSum4(nums, target):
    hashmap={}
    for i,num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i,hashmap.get(target - num)]
        hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


if __name__ == '__main__':
	nums=[2, 7, 11, 15]
	target=9
	print(twoSum1(nums, target))
	print(twoSum2(nums, target))
	print(twoSum3(nums, target))
	print(twoSum4(nums, target))
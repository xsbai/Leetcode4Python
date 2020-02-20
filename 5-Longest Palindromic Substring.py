# coding=utf-8

"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。

示例 2：
    输入: "cbbd"
    输出: "bb"

"""

"""
方法一：暴力匹配 （Brute Force）
根据回文子串的定义，枚举所有长度大于等于 22 的子串，依次判断它们是否是回文；
在具体实现时，可以只针对大于“当前得到的最长回文子串长度”的子串进行“回文验证”；
在记录最长回文子串的时候，可以只记录“当前子串的起始位置”和“子串长度”，不必做截取。这一步我们放在后面的方法中实现。

方法二：动态规划
依然从回文串的定义展开讨论：
1、如果一个字符串的头尾两个字符都不相等，那么这个字符串一定不是回文串；
2、如果一个字符串的头尾两个字符相等，才有必要继续判断下去。
（1）如果里面的子串是回文，整体就是回文串；
（2）如果里面的子串不是回文串，整体就不是回文串。
即在头尾字符相等的情况下，里面子串的回文性质据定了整个子串的回文性质，这就是状态转移。因此可以把“状态”定义为原字符串的一个子串是否为回文子串。

方法三：中心扩散法
暴力法采用双指针两边夹，验证是否是回文子串。
除了枚举字符串的左右边界以外，比较容易想到的是枚举可能出现的回文子串的“中心位置”，从“中心位置”尝试尽可能扩散出去，得到一个回文串。
因此中心扩散法的思路是：遍历每一个索引，以这个索引为中心，利用“回文串”中心对称的特点，往两边扩散，看最多能扩散多远。
在这里要注意一个细节：回文串在长度为奇数和偶数的时候，“回文中心”的形式是不一样的。
奇数回文串的“中心”是一个具体的字符，例如：回文串 "aba" 的中心是字符 "b"；
偶数回文串的“中心”是位于中间的两个字符的“空隙”，例如：回文串串 "abba" 的中心是两个 "b" 中间的那个“空隙”。


"""
class Solution:
    # 暴力匹配（超时）
    def longestPalindrome1(self, s: str) -> str:
        # 特判
        size = len(s)
        if size < 2:
            return s

        max_len = 1
        res = s[0]

        # 枚举所有长度大于等于 2 的子串
        for i in range(size - 1):
            for j in range(i + 1, size):
                if j - i + 1 > max_len and self.__valid(s, i, j):
                    max_len = j - i + 1
                    res = s[i:j + 1]
        return res

    def __valid(self, s, left, right):
        # 验证子串 s[left, right] 是否为回文串
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    # 动态规划
    def longestPalindrome2(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]


    # 中心扩散
    def longestPalindrome3(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        # 至少是 1
        max_len = 1
        res = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res

    def __center_spread(self, s, size, left, right):
        """
        left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
        """
        i = left
        j = right

        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i - 1



if __name__ == '__main__':
    s = "babad"
    print(solution.longestPalindrome1(s))
    print(solution.longestPalindrome2(s))
    print(solution.longestPalindrome3(s))
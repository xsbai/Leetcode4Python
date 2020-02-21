# coding=utf-8

"""
6. Z 字形变换
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
示例 1:
    输入: s = "LEETCODEISHIRING", numRows = 3
    输出: "LCIRETOESIIGEDHN"

示例 2:
    输入: s = "LEETCODEISHIRING", numRows = 4
    输出: "LDREOEIIECIHNTSG"

"""

"""
字符串 s 是以 ZZ 字形为顺序存储的字符串，目标是按行打印。
设 numRows 行字符串分别为s1,s2...sn，则容易发现：按顺序遍历字符串s时，每个字符c在Z字形中对应的 行索引 先从 s1 增大至sn,再从 sn减小至s1,如此反复。
解决方案为：模拟这个行索引的变化，在遍历 s 中把每个字符填到正确的行 res[i] 。
按顺序遍历字符串 s；
1.res[i] += c： 把每个字符 c 填入对应行 si
2.i += flag： 更新当前字符 c 对应的行索引；
3.flag = - flag： 在达到 ZZ 字形转折点时，执行反向。

"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)

if __name__ == '__main__':
    s = "LEETCODEISHIRIN"
    numRows = 3
    print(solution.convert(s,numRows))
# coding=utf-8

"""
2. 两数相加

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#定义链表
class LinkList:
    def __init__(self):
        self.head=None
 
    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r=self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r
    def printlist(self,head):
        if head == None: return
        node = head
        while node != None :
            print(node.val,end=' ')
            node = node.next


class Solution:
    """
    方法1：链表方法
    不断的遍历两个链表，每次遍历都将链表a和链表b的值相加，再赋给链表a。如果有进位我们还需要记录一个进位标志。
    循环的条件是链表a不为空或者链表b不为空，这样当整个循环结束时，链表就被串起来了。
    当循环结束时，如果进位标志>0还需要处理下边界条件。
    我们不用生成一个新的节点，直接将两个节点相加的值赋给节点a
    """

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 定义一个进位标志
        a,b,p,carry = l1,l2,None,0
        while a or b:
            # a和b节点的值相加，如果有进位还要加上进位的值
            val = (a.val if a else 0)+(b.val if b else 0)+carry
            # 根据val判断是否有进位,不管有没有进位，val都应该小于10
            carry,val = int(val/10) if val>=10 else 0, val%10
            p,p.val = a if a else b,val
            # a和b指针都前进一位
            a,b = a.next if a else None,b.next if b else None
            # 根据a和b是否为空，p指针也前进一位
            p.next = a if a else b
        # 不要忘记最后的边界条件，如果循环结束carry>0说明有进位需要处理这个条件    
        if carry:
            p.next = ListNode(carry)
        # 每次迭代实际上都是将val赋给a指针的，所以最后返回的是l1    
        return l1


    """
    方法2:递归实现
    递归出口条件：链表a和链表b都为空时
    将两个链表的值相加，再赋给链表a
    这里需要注意第二个条件，因为进位标志需要通告下一层递归函数，所以需要有一个单独的变量作为记录。
    函数内部的进位标志判断，val计算的方式和迭代版本是类似的。
    调用下一层递归的时候，传递的参数是a.next和b.next。
    这里还需要注意一个细节，如果a，b两个链表不一样长，意味递归到一定的层次时，某个链表会出现null，这时需要做一个补0的操作，创建一个新的节点赋给节点为空的链表。
    """
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 主要逻辑都在内部函数中实现
        def add(a,b,carry):
            # 递归的终止条件是a和b都为空
            # 如果carry大于0需要返回一个进位标志
            if not (a or b):
                return ListNode(1) if carry else None
            # 如果a为空则将ListNode(0)赋给a，对于b也是
            a = a if a else ListNode(0)
            b = b if b else ListNode(0)
            #处理val，以及进位标志
            val = a.val + b.val + carry
            carry = 1 if val>=10 else 0
            a.val = val%10
            # 现在a的值就是两个节点相加后的和了
            # 之后再次递归计算a.next和b.next
            a.next = add(a.next,b.next,carry)
            return a
        return add(l1,l2,0)


if __name__ == '__main__':
    solution = Solution()
    l1=[2, 4, 3]
    l2=[5, 6, 4]
    link=LinkList()
    l1=link.initList(l1)
    l2=link.initList(l2)
    # 注意l1 l2穿参为地址，分开测试
    #print(link.printlist(solution.addTwoNumbers1(l1, l2)))
    print(link.printlist(solution.addTwoNumbers2(l1, l2)))
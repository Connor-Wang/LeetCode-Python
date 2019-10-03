# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        jinwei = 0
        ret = ListNode(0)
        lastNode = ret
        while(l1 or l2 or jinwei):
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            jinwei, temp = divmod(jinwei + temp1 + temp2, 10)
            lastNode.next = ListNode(temp%10)
            lastNode = lastNode.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return ret.next

def generateList(list: list) -> ListNode:
    preNode = ListNode(0)
    lastNode = preNode
    for val in list:
        lastNode.next = ListNode(val)
        lastNode = lastNode.next
    return preNode.next

def printList(list: ListNode):
    while(list.next != None):
        print(list.val, "-> ", end="")
        list = list.next
    print(list.val)

if __name__ == "__main__":
    l1 = generateList([9, 1, 6])
    l2 = generateList([0])
    printList(l1)
    printList(l2)
    s = Solution()
    sum = s.addTwoNumbers(l1, l2)
    printList(sum)
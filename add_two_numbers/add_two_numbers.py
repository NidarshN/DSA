class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getNum(self, l):
        num_res = 0
        ptr = l
        i = 0
        while(ptr!=None):
            num_res = (ptr.val * (10**i)) + num_res
            i+=1
            ptr = ptr.next
        return num_res
    
    def printList(self, l):
        while(l!=None):
            print("->", l.val)
            l = l.next

    def getList(self, num):
        res = ListNode()
        ptr = res
        while(num > 0):
            ptr.val = num % 10
            num //= 10
            if(num > 0):
                ptr.next = ListNode()
                ptr = ptr.next
            else:
                break
        return res

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.getNum(l1)
        num2 = self.getNum(l2)
        res = self.getList(num1 + num2)
        return res
    
if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    solution = Solution()
    solution.printList(solution.addTwoNumbers(l1, l2))




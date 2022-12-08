# yijinKim
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        temp = ListNode(-1)
        temp.next = head
        
        back = temp
        front = temp
        
        for i in range(n): 
            front = front.next
            
        while front.next != None:
            front = front.next
            back = back.next
        
        back.next = back.next.next
        
        return temp.next
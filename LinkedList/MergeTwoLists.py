class ListNode:
    def __init__(self, val=0, next=Node):
        self.val = val
        self.next = next
        
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    new_list = new_head = ListNode(0)
    
    while list1 and list2:
        if list1.val <= list2.val:
            new_head.next = list1
            list1 = list1.next
        else:
            new_head.next = list2
            list2 = list2.next
        new_head = new_head.next
        
    new_head.next = list1 or list2
    
    return new_list.next
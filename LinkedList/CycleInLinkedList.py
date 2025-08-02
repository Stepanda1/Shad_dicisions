# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None
#         
# class DoubleLinkedList:
#     def __init__(self, value=5):
#         self.head = Node(value)
#         self.tail = self.head
#         self.length = 1
#         
#     def append(self, value):
#         newNode = Node(value)
#         newNode.prev = self.tail
#         self.tail.next = newNode
#         self.tail = newNode
#         self.length += 1
#         return self
# 
#     def prepend(self, value):
#         newNode = Node(value)
#         self.head.prev = newNode
#         newNode.next = self.head
#         self.head = newNode
#         self.length += 1
#         return self
# 
#     def _print(self):
#         if not self.head:
#             print('List is empty')
#             return
#         
#         print(f'Head: {self.head.value}')
#         currentNode = self.head
#         while currentNode.next:
#             print(currentNode.value)
#             currentNode = currentNode.next
#         print(currentNode.value)
#         print(f'Tail: {self.tail.value}')
#         
#     def reverse(self):
#         if not self.head.next:
#             return self.head
#         first = self.head
#         self.tail = self.head
#         second = first.next
#         while second:
#             temp = second.next
#             second.next = first
#             first = second
#             second = temp
#         self.head.next = None
#         self.head = first
#         return self
#     
# dll = DoubleLinkedList()
# dll.append(10).append(20).append(30)
# dll._print()
# dll.reverse()
# dll._print()

class Node:
    def __init(self, val=0, next=None):
        self.val = val
        self.next = next
        
def hasCycle(self, head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

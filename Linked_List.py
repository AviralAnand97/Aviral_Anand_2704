class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        
        count = 0 
        connected = False

        while head:
            if head.val in nums and not connected:
                connected = True
                count += 1
            elif head.val not in nums and connected:
                connected = False

            head = head.next

        return count 
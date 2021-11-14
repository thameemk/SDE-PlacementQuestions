#  [Only For Educational Purpose]
#  Project : SDE-Placement Questions
#  Filename : two_sum.py
#  Author : thameem
#  Created  time : Sun, 14 Nov 2021 at 11:34 PM India Standard Time
#  Last modified time : Sun, 14 Nov 2021 at 11:34 PM India Standard Time

from beartype import beartype


class Solution:
    
    @staticmethod
    @beartype
    def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = l1[::-1]
        l2 = l2[::-1]
        
        number1 = ""
        for i in range(len(l1)):
            number1 =+ str(l1[i])
        
        number1 = int(number1)
        
        number2 = ""
        for j in range(len(l2)):
            number2 =+ str(l2[i])
    
        number2 = int(number2)
      
 

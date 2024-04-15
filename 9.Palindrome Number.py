#####My Answer#####
class Solution:
    def isPalindrome(self, x: int) -> bool:

        str_x = str(x)

        rev_str = ""
        for i in str_x:
            rev_str = i + rev_str

        if str_x == rev_str:
            return True
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_x=str(x)[::-1]
        
        if reverse_x == str(x):
            return True
        else:
            return False
        
# H1 Beware of overflow when you reverse the integer.


# Intuition:
# The intuition behind this code is to reverse the entire input number and check if the reversed number is equal to the original number. If they are the same, then the number is a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x

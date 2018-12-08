




# clean solution
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True


'''
three things to be noted: 
1. check if l<r before each time l,r change
2. compare after char is turned into lower case
3. a simple palindrome problem can be solve by s==s[::-1]
odd or even number of char is not a problem for in odd cases, 
the last comparison happens when r=l, while in even cases, 
the last comparison happens when r=l+1
'''


# short and tricky one
class Solution:
def isPalindrome(self, s):
    newS= [i.lower() for i in s if i.isalnum()]
    return newS == newS[::-1]
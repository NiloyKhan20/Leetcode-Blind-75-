'''This solution uswes the expand around center approach to find the longest palindromic substring in a given string.
The time comiplexity is O(n^2) and the space complexity is O(1)
'''


class Solution(object):
    def longestPalindrome(self,s):
        longest=0 # Initialize the longest length to 0
        res="" # Empty string that is going to hold the resultant substring
        for character in range (len(s)):
            left,right=character,character # Set left and right pointers to the current character
            while(left>=0 and right<len(s) and s[left]==s[right]):
                if(right-left+1>longest): # Check if the current palindrome is longer than the previous longest
                    longest=right-left+1 # Update the longest length
                    res=s[left:right+1]# Update the resultant substring
          
                left-=1 # Expand the left pointer
                right+=1#` Expand the right pointer
        

        for character in range (len(s)):
                left,right=character,character+1 # Do the same for even length palindromes with a little change by adding +1 to the right pointer
                while(left>=0 and right<len(s) and s[left]==s[right]):
                    if(right-left+1>longest):
                        longest=right-left+1 
                        res=s[left:right+1]
                    left-=1
                    right+=1
        return res            



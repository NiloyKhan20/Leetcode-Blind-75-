# This solution uses the sliding window technique to find the length of the longest substring without repeating characters. 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashmap={} # to check duplicates of characters 
        left=0# left pointer of the window 
        max_length=0 # this keeps track of the maximum length 

        for right in range(len(s)):
            if(s[right] in hashmap and hashmap[s[right]]>=left):
                left=hashmap[s[right]]+1
            hashmap[s[right]]=right
            max_length=max(max_length,right-left+1)    
        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # get the frequency of each character in the string
        # check for a character with frequency = 1
        # return the first character
        
        freq = {}
        for char in s:
            if char in freq:
                freq[char] = freq[char] + 1
            else:
                freq[char] = 1
        
        for i, char in enumerate(s):
            if (freq[char] == 1):
                return i
            
        return -1
            
            

        
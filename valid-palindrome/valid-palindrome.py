class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # convert all the characters in lowercase using the .lower() method
        # remove all the non-alphanumeric characters using the .isalnum() method
        
        s1 = s.lower()
        getVals = list([val for val in s1 if val.isalnum()])
        resultstr = "".join(getVals)
        
        n = len(resultstr)
        i = 0
        j = n-1
        
        while i< j:
            if (resultstr[i] !=resultstr[j]):
                return False
            i = i+1
            j = j-1
                
        return True
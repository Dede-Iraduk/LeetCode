class Solution:
    def reverse(self, x: int) -> int:
        reversedint = 0
        if x < 0:
            reversedint = int(str(x)[1:][::-1]) * -1
           
        else:
            reversedint = int(str(x)[::-1])
        
        if reversedint > 2 ** 31 - 1 or reversedint < -2 ** 31:
            return 0
        
        return reversedint 



# if the number does have a negative sign
# casting into string, reverse it , revert it back to int and multiply it by -1
# if not casting into string, reverse it and return integer
# if reversed string is outside range, return 0
        
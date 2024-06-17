class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # create a string called resp
        # traverse the 3 strings while comparing characters at each index
        # return the prefix stored in resp
        resp = ""
        minlen = len(strs[0])
        for s in strs:
            currlen = len(s)
            if currlen < minlen:
                minlen = currlen

        for i in range(minlen):
            currchar = strs[0][i]
            if all(s[i] == currchar for s in strs):
                resp += currchar
            else:
                    break
        return resp 
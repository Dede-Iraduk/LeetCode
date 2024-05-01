class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        res = 0

        hashmap = {}

        for i in arr:
            if i not in hashmap:
                hashmap[i]=0
            hashmap[i]+=1

        for key in hashmap:
            if (key+1) in hashmap:
                res+=hashmap[key]

        return res   
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap= {}
        count = len(ransomNote)
        for i in magazine:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] = 1
        for j in ransomNote:
            if j in hashmap:
                hashmap[j] -= 1
            else:
                hashmap[j] = -1
                
        if any(count < 0 for count in hashmap.values()):
            return False
        return True


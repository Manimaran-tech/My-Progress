class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_note = Counter(magazine)
        ran_note = Counter(ransomNote)
        for i in ran_note:
            if ran_note[i] > mag_note[i]:
                return False
        return True 
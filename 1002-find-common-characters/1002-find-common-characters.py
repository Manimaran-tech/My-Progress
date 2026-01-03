class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])   # count chars of first word
        
        for word in words[1:]:
            common &= Counter(word)  # keep minimum frequency
        
        result = []
        for ch, freq in common.items():
            result.extend([ch] * freq)
        
        return result
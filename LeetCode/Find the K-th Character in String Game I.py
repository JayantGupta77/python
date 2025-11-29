class Solution(object):
    def kthCharacter(self, k):
        
        word = "a"
        
        while len(word) < k:
            next_str = ""
            for ch in word:
                if ch == 'z':
                    next_str += 'a'
                else:
                    next_str += chr(ord(ch) + 1)
            
            word += next_str
        
        return word[k-1]
        
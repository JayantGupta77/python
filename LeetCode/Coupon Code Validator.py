from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        
        categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        category_order = {cat: i for i, cat in enumerate(categories)}
        
        # Helper function to check if code is valid
        def is_valid_code(s: str) -> bool:
            if not s:
                return False
            for ch in s:
                if not (ch.isalnum() or ch == "_"):
                    return False
            return True
        
        # Collect valid coupons
        valid = []
        for i in range(n):
            if isActive[i] and is_valid_code(code[i]) and businessLine[i] in category_order:
                valid.append((category_order[businessLine[i]], code[i]))
        
        # Sort by category order, then lexicographically by code
        valid.sort(key=lambda x: (x[0], x[1]))
        
        # Extract sorted codes
        return [c for _, c in valid]

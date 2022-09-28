class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        S_out, T_out = [], []
        
        for char in s:
            if char == '#':
                if S_out: S_out.pop()
            else:
                S_out.append(char)
                
        for char in t:
            if char == '#':
                if T_out: T_out.pop()
            else:
                T_out.append(char)
        
        return S_out == T_out
            
        
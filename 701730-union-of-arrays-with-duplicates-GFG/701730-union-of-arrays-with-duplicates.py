class Solution:    
    def findUnion(self, a, b):
        # code here
        set1 = set()
        set2 = set()
        set1.update(a)
        set2.update(b)
        
            
            
        return list(set1 | set2)
        
            
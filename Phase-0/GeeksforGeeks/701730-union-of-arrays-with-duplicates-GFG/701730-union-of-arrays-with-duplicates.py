class Solution:    
    def findUnion(self, a, b):
        # code here
        set1 = set()
        set2 = set()
        
        for i in range(len(a)):
            set1.add(a[i])
        
        for i in range(len(b)):
            set2.add(b[i])
        
        output = list(set1 | set2)
        output.sort()
        
        return output
class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        reverse = 0
        if x < 0:           
            x = -1 * x
            flag = True
        
        while x != 0:
            reverse = reverse * 10 +  x % 10 
            x = x // 10
        if flag:
            reverse = -1 * reverse
        if reverse < (-2)**31 or reverse > (2**31-1):
            return 0
        return reverse
        
            
            

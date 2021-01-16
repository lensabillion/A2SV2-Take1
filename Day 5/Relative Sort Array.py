class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        ans = []
        cnt = [0] *( max(arr1)+1)
        for i in arr1:
            cnt[i] += 1
        for n in arr2:
            while cnt[n] > 0:
                ans.append(n)
                cnt[n] -= 1
        for l in range(len(cnt)):
            if  cnt[l] != 0:
                for k in range(cnt[l]):
                    ans.append(l)
        return ans
    
     

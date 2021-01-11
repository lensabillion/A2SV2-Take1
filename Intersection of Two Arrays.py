class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rlst = []
        
        
        if len(nums1) <= len(nums2):
            min =set(nums1)
            max= set(nums2)
        else:
            min = set(nums2)
            max =set(nums1)
        for i in min:
            if i in max:
                rlst.append(i)
        return rlst
        

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        total = len1 + len2
        if((len1 + len2) % 2 == 1):
            return self.findKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, total / 2)
        else :
            return (self.findKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, total / 2 - 1) + self.findKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, total / 2)) * 0.5

    def findKth(self, nums1, left1, right1, nums2, left2, right2, k):
        len1 = right1 - left1 + 1
        len2 = right2 - left2 + 1
        if len1 == 0:
            return nums2[left2 + k]
        if len2 == 0:
            return nums1[left1 + k]
        if k == 0:
            return min(nums1[left1], nums2[left2])
            
        i = int(len1 / (len1 + len2) * k)
        j = k - i - 1
        
        mid1 = min(left1 + i, right1)
        mid2 = min(left2 + j, right2)
        
        if(nums1[mid1] < nums2[mid2]):
            k = k - (mid1 - left1 + 1)
            left1 = mid1 + 1
            right2 = mid2
        else:
            k = k - (mid2 - left2 + 1)
            left2 = mid2 + 1
            right1 = mid1
        return self.findKth(nums1, left1, right1, nums2, left2, right2, k)


lst1 = [2, 3]
lst2 = [2, 3]

solution = Solution()
print solution.findMedianSortedArrays(lst1, lst2)


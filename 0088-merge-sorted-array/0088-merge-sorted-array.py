class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Pointers
        i = m - 1  # Last element of nums1's actual data
        j = n - 1  # Last element of nums2
        k = m + n - 1  # Last index in nums1 (where we insert)

        # Merge from the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements left, put them in nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

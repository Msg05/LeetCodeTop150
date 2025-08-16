class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0  # left pointer (last unique element)

        for j in range(1, len(nums)):     # right pointer scans ahead
            if nums[j] != nums[i]:        # found a new unique element
                i += 1                    # move left pointer
                nums[i] = nums[j]         # place unique element at new position

        return i + 1  # number of unique elements

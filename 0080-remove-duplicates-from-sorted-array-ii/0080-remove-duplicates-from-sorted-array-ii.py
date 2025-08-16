class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        i = 2  # start from index 2 since first two elements are always allowed
        for j in range(2, len(nums)):
            # checking for new element
            # nums[i-2] is the element two positions before i
            # If nums[j] != nums[i-2], that means nums[j] is not a 3rd+ duplicate
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]   # copy nums[j] into the "write" spot
                i += 1              # move the write pointer forward

        return i  # i is the length of valid (deduplicated) part

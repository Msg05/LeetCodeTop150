class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        class Solution(object):

        if len(nums) <= 2:
            return len(nums)

        i = 2  # start from index 2 since first two elements are always allowed
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:  # checking for new element->i,i+1 will contain same element->so i-2=(i,i+1) going back to i -> that means if j is not equal to i and i+1, then put j in place of i
                nums[i] = nums[j]       # place valid element
                i += 1                  # move write pointer

        return i  # length of valid part

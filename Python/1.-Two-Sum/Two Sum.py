class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Subtract the target value from dictionary
        new_target = [target - x for x in nums]

        # Create hash maps with keys.
        nums = dict(enumerate(nums))
        new_target_dic = dict(enumerate(new_target))

        # Iterate in the hash map.
        for key_target,digit_target in new_target_dic.iteritems():
            if digit_target in nums.values():
                key = [key for key, value in nums.items() if value == digit_target][0]

                # The matching can't be with the same number!
                if key!=key_target:
                    index = [min(key,key_target),max(key,key_target)]

        return index

nums = [3,2,4]
target = 6

C=Solution()
print C.twoSum(nums,target)


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_target = [target - x for x in nums]

        # Create hash maps with keys.
        nums = dict(enumerate(nums))
        new_target_dic = dict(enumerate(new_target))

        # Create inverse dictionary
        ivd_new_target_dic = {v: k for k, v in new_target_dic.items()}

        # Iterate in the hash map.
        for key, digit in nums.items():
            if digit in ivd_new_target_dic.keys():

                # Find the target key
                key_target = ivd_new_target_dic[digit]

                # The matching can't be with the same number!
                if key != key_target:
                    index = [key, key_target]

                    # Since the matching is unique so we use break!
                    break

        return index



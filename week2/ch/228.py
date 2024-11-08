class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        nums = nums+[-float('inf')]
        starting_number = nums[0]
        if len(nums) == 1:
            return [str(nums[0])]
        cur_number = starting_number
        ret = []
        for idx in range(1,len(nums)):
            if cur_number + 1 == nums[idx]:
                cur_number +=1
            else:
                if starting_number == cur_number:
                    ret.append(f"{starting_number}")
                else:
                    ret.append(f"{starting_number}->{cur_number}")
                starting_number = nums[idx]
                cur_number = starting_number
        return ret

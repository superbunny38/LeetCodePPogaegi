class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start_idx, end_idx = 0,n-1
        pivot_idx = int((start_idx+end_idx)/2)
        
        while start_idx<=end_idx:
            # print(f"\nchecking... start_idx:{start_idx} end_idx:{end_idx}")
            pivot_idx = int(start_idx/2+end_idx/2)
            # print("pivot_idx:",pivot_idx)
            if nums[pivot_idx] == target:
                return pivot_idx
            if nums[start_idx]<=nums[pivot_idx]:#if left half is sorted
                if nums[start_idx]<=target<=nums[pivot_idx]:#if pivot falls within the range
                    # print("nums[start_idx]<nums[pivot_idx]")
                    # print("nums[start_idx]<target<nums[pivot_idx]")
                    end_idx = pivot_idx-1
                else:#if the pivot is not sorted_left pivot
                    # print("nums[start_idx]<nums[pivot_idx]")
                    # print("else")
                    start_idx = pivot_idx+1
                continue
            else:#if right half is sorted
                if nums[pivot_idx]<=target<=nums[end_idx]:
                    # print("else")
                    # print("nums[pivot_idx]<target<nums[end_idx]")
                    start_idx = pivot_idx+1
                else:
                    # print("else")
                    # print("else")
                    end_idx = pivot_idx-1
        # print(f"exited.. start_idx:{start_idx} end_idx:{end_idx}")
        return -1
                    

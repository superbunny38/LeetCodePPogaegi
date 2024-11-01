class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        for i in range(len(nums) - k + 1):
            subarray = nums[i:i + k]
            sub_counter = Counter(subarray)
            if len(sub_counter) < x:
                answer.append(sum(subarray))
                continue
            key_val_pairs = list(sub_counter.items())
            key_val_pairs.sort(key = lambda x: (-x[1], -x[0]))
            sums = 0
            for j in range(x):
                sums += key_val_pairs[j][0] * key_val_pairs[j][1]
            answer.append(sums)
        return answer

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter = Counter(s1)
        window_counter = Counter(s2[:len(s1)])
        if counter == window_counter:
            return True
        for i in range(len(s2) - len(s1)):
            window_counter[s2[i]] -= 1
            window_counter[s2[len(s1) + i]] += 1
            if counter == window_counter:
                return True

        return False

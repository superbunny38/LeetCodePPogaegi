class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        left, right = 0, len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = []
        for mat in matrix:
            flattened += mat
        
        def search(arr):
            if len(arr) <= 2:
                if target not in arr:
                    return False
                else:
                    return True
            mid_point = int(len(arr)//2)
            if arr[mid_point] == target:
                return True
            elif arr[mid_point]<target:
                return search(arr[mid_point+1:])
            else:
                return search(arr[:mid_point])
        return search(flattened)

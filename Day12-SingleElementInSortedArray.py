class SingleElementInSortedArray:
    def singleNonDuplicate(self, nums):
        # return (sum(set(nums))*2)-sum(nums) # 1-line solution O(n)
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid];
            elif nums[mid] == nums[mid + 1] and mid % 2 == 0:
                start = mid + 1
            elif nums[mid] == nums[mid - 1] and mid % 2 == 1:
                start = mid + 1
            else:
                end = mid - 1
        return nums[start]


obj = SingleElementInSortedArray()
print(obj.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(obj.singleNonDuplicate([1, 1, 2]))

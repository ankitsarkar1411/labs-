class PairFinder:
    def find_pair(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        return []


print(PairFinder().find_pair([2, 7, 11, 15], 9))  

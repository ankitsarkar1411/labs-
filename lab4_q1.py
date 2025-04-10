from itertools import chain, combinations

class SubsetGenerator:
    def get_subsets(self, nums):
        return list(map(list, chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))))

print(SubsetGenerator().get_subsets([1, 2, 3]))

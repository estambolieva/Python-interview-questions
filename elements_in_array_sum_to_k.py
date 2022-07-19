### TASK DESCRIPTION

# Given a number K and an array of unique numbers ARR, write an application to find and print all the pairs in N that have an equal sum to K
# Write unit tests to test your code

### TASK DESCRIPTION END

from itertools import permutations
import unittest

# finds all groups of numbers which sum up to K
def find_pairs_that_sum_to_k_1(arr, k):
	pairs = set()

	for n in range(len(arr) + 1):
		for perm in permutations(arr, n):
			if sum(perm) == k:
				pairs.add(perm)

	print(pairs)
	return pairs

# finds all pairs of numbers which sum up ot K
def find_pairs_that_sum_to_k_2(arr, k): 
	pairs = set()

	set_of_arr = set(arr)

	for num in arr:
		if (k-num) in set_of_arr:
			pairs.add((num, k-num))

	return pairs


class TestSum(unittest.TestCase):

    def test_sum_1(self): # find_pairs_that_sum_to_k_1
    	correct = {(3, 1, 4), (6, 2), (7, 1), (4, 3, 1), (1, 3, 4), (1, 4, 3), (1, 7), (2, 6), (3, 4, 1), (4, 1, 3)}
    	self.assertEqual(find_pairs_that_sum_to_k_1([1,2,3,4,6,7], 8), correct, "Should be the same two sets")

    def test_sum_2(self):
    	correct = {(4, 4), (6, 2), (7, 1), (1, 7), (2, 6)}
    	self.assertEqual(find_pairs_that_sum_to_k_2([1,2,3,4,6,7], 8), correct, "Should be the same two sets")


if __name__ == '__main__':
    unittest.main()
    # print(find_pairs_that_sum_to_k_2([1,2,3,4,6,7], 8))

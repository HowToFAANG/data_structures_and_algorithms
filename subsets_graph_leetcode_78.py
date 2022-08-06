def subsets(nums):
	# idea: bfs (or dfs) over "solution graph"
	all_sets = []
	queue = []
	queue.append((0, []))

	while queue:
		cur_index, cur_set = queue.pop(0)
		num_to_add = nums[cur_index]
		next_index = cur_index + 1

		# add the new num
		set_with_addition = list(cur_set)
		set_with_addition.append(num_to_add)
		if (next_index < len(nums)):
			queue.append((next_index, set_with_addition))
		else:
			all_sets.append(set_with_addition)

		# don't add the new num
		set_without_addition = list(cur_set)
		if (next_index < len(nums)):
			queue.append((next_index, set_without_addition))
		else:
			all_sets.append(set_without_addition)

	return all_sets

print(subsets([1,2,3]))

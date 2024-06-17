def sort_tuples_by_last_element(tuples_list):
    # Sort the list of tuples based on the last element (index -1)
    sorted_list = sorted(tuples_list, key=lambda x: x[-1])
    return sorted_list

# Sample list of tuples
sample_list = [(1, 2), (3, 2), (4, 4), (2, 1), (5, 2)]

# Get the sorted result
result = sort_tuples_by_last_element(sample_list)

print(result)

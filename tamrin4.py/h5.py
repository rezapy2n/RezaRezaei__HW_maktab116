def sort_tuples_by_last_element(tuples_list):
   
    sorted_list = sorted(tuples_list, key=lambda x: x[-1])
    return sorted_list


sample_list = [(1, 2), (3, 2), (4, 4), (2, 1), (5, 2)]


result = sort_tuples_by_last_element(sample_list)

print(result)

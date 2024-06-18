def multiply_list(my_list):
    result = 1
    for x in my_list:
        result *= x
    return result

sample_list = [7, -1, 3, 2, 8]
print(multiply_list(sample_list))  

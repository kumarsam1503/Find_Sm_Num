def find_smallest_number(lst):
    smallest = lst[0]

    for num in lst[1:]:
        if num < smallest:
            smallest = num

    # Return the smallest number
    return smallest


# Test the function with the given input list
list1 = [5, 7, 9, 14, 10, 20, 4]
print("The smallest number in list1 is:", find_smallest_number(list1))

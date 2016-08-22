"""
Filter:
9, [3, 2, 6]    # False  [3]
12, [3, 2, 6]   # True   [3, 2, 6]

Map:
9, [3, 2, 6]    # False  [True, False, False]
12, [3, 2, 6]   # True   [True, True, True] 

"""
def is_number_divisible_by_terms(number, a_list_of_terms):
    return len([term for term in a_list_of_terms if number % term == 0]) == len(a_list_of_terms)


def divisible_numbers(a_list, a_list_of_terms):
    return [
        number for number in a_list
        if is_number_divisible_by_terms(number, a_list_of_terms)
    ]

assert is_number_divisible_by_terms(12, [2, 3]) is True
assert is_number_divisible_by_terms(9, [3, 2]) is False

print("Everything worked!")


# is_number_divisible_by_terms(12, [2, 3])  # True
# is_number_divisible_by_terms(9, [2, 3])  # False



# my_list = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# terms = [2, 3]


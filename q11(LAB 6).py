def has_common_member(list1, list2):
    return any(item in list2 for item in list1)

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 8]
print(has_common_member(list1, list2))  # Output: True
